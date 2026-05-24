from __future__ import annotations

import io
import json
from typing import Optional

from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI, Header, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, ConfigDict, Field
from pypdf import PdfReader

import agent
import db

db.init_db()

MAX_RESUME_BYTES = 5 * 1024 * 1024

app = FastAPI(title="CareerCompass API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_methods=["GET", "POST", "PUT"],
    allow_headers=["Authorization", "Content-Type"],
)


class Message(BaseModel):
    role: str = Field(max_length=20)
    content: str = Field(max_length=8000)


class Profile(BaseModel):
    situation: str = Field(default="", max_length=40)
    skills: str = Field(default="", max_length=1000)
    interests: str = Field(default="", max_length=1000)
    goals: str = Field(default="", max_length=1000)
    experience_level: str = Field(default="", max_length=40)
    desired_roles: str = Field(default="", max_length=1000)


class SignupRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    username: str = Field(min_length=3, max_length=32, pattern=r"^[A-Za-z0-9_.-]+$")
    password: str = Field(min_length=8, max_length=128)


class LoginRequest(BaseModel):
    username: str = Field(min_length=1, max_length=32)
    password: str = Field(min_length=1, max_length=128)


class InterviewRequest(BaseModel):
    history: list[Message] = Field(default=[], max_length=40)
    stage: str = Field(default="recent_grad", max_length=40)
    assistant_id: Optional[str] = Field(default=None, max_length=100)
    memory_on: bool = False


class DiagnoseRequest(BaseModel):
    transcript: str = Field(default="", max_length=20000)
    resume: str = Field(default="", max_length=50000)
    stage: str = Field(default="recent_grad", max_length=40)
    assistant_id: Optional[str] = Field(default=None, max_length=100)
    memory_on: bool = False
    messages: list[Message] = Field(default=[], max_length=40)


class RoadmapRequest(BaseModel):
    path_key: str
    have_skills: list[str] = []
    context: str = ""


def _user_from_header(authorization: Optional[str]) -> Optional[dict]:
    if not authorization or not authorization.startswith("Bearer "):
        return None
    token = authorization[len("Bearer ") :].strip()
    return db.get_user_by_token(token) if token else None


def _profile_of(user: dict) -> dict:
    return {f: user.get(f, "") for f in (*db.PROFILE_FIELDS, "last_summary")}


def _ai_result(fn):
    try:
        return fn()
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc))


@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.post("/api/auth/signup")
def signup(req: SignupRequest):
    user = db.create_user(req.username, req.password)
    if user is None:
        raise HTTPException(status_code=409, detail="Username already taken")
    return user


@app.post("/api/auth/login")
def login(req: LoginRequest):
    user = db.authenticate(req.username, req.password)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    db.increment_visits(user["id"])
    return user


@app.get("/api/me")
def me(authorization: Optional[str] = Header(None)):
    user = _user_from_header(authorization)
    if user is None:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return user


@app.put("/api/profile")
def update_profile(req: Profile, authorization: Optional[str] = Header(None)):
    user = _user_from_header(authorization)
    if user is None:
        raise HTTPException(status_code=401, detail="Not authenticated")
    db.update_profile(user["id"], req.model_dump())
    return db.get_user_by_token(user["token"])


@app.post("/api/interview")
def interview(req: InterviewRequest, authorization: Optional[str] = Header(None)):
    history = [{"role": m.role, "content": m.content} for m in req.history]
    if not history:
        history = [{"role": "user", "content": "Start the interview with your first question."}]
    user = _user_from_header(authorization)
    if user:
        situation = user.get("situation") or req.stage or "recent_grad"
        if not user.get("situation") and req.stage:
            db.set_situation(user["id"], req.stage)
        result = _ai_result(
            lambda: agent.interview_turn(
                history,
                situation,
                user.get("assistant_id"),
                memory_on=True,
                profile=_profile_of(user),
                returning=bool(user.get("last_summary")),
            )
        )
        if result.get("assistant_id") and not user.get("assistant_id"):
            db.set_assistant_id(user["id"], result["assistant_id"])
        return result
    return _ai_result(
        lambda: agent.interview_turn(history, req.stage, req.assistant_id, req.memory_on)
    )


@app.post("/api/diagnose")
def diagnose(req: DiagnoseRequest, authorization: Optional[str] = Header(None)):
    user = _user_from_header(authorization)
    if user:
        data = _ai_result(
            lambda: agent.diagnose(
                req.transcript,
                req.resume,
                user.get("situation") or "recent_grad",
                user.get("assistant_id"),
                memory_on=True,
                profile=_profile_of(user),
            )
        )
        db.set_last_summary(user["id"], data.get("summary", ""))
        inferred_profile = data.get("inferred_profile")
        if isinstance(inferred_profile, dict):
            db.save_inferred_profile(user["id"], inferred_profile)
        messages_json = json.dumps([m.model_dump() for m in req.messages])
        db.save_session(
            user["id"], data.get("summary", ""), messages_json, json.dumps(data)
        )
        return data
    return _ai_result(
        lambda: agent.diagnose(
            req.transcript, req.resume, req.stage, req.assistant_id, req.memory_on
        )
    )


@app.get("/api/sessions")
def sessions(authorization: Optional[str] = Header(None)):
    user = _user_from_header(authorization)
    if user is None:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return db.list_sessions(user["id"])


@app.get("/api/sessions/{session_id}")
def session_detail(session_id: int, authorization: Optional[str] = Header(None)):
    user = _user_from_header(authorization)
    if user is None:
        raise HTTPException(status_code=401, detail="Not authenticated")
    s = db.get_session(user["id"], session_id)
    if s is None:
        raise HTTPException(status_code=404, detail="Session not found")
    return {
        "id": s["id"],
        "summary": s["summary"],
        "created_at": s["created_at"],
        "messages": json.loads(s["messages_json"]),
        "diagnosis": json.loads(s["diagnosis_json"]),
    }


@app.post("/api/roadmap")
def roadmap(req: RoadmapRequest):
    return _ai_result(lambda: agent.build_roadmap(req.path_key, req.have_skills, req.context))


@app.post("/api/parse-resume")
async def parse_resume(file: UploadFile):
    if file.content_type not in ("application/pdf", "application/octet-stream"):
        raise HTTPException(status_code=400, detail="Only PDF files are accepted")
    data = await file.read()
    if len(data) > MAX_RESUME_BYTES:
        raise HTTPException(status_code=413, detail="Resume file is too large")
    try:
        reader = PdfReader(io.BytesIO(data))
        text = "\n".join(page.extract_text() or "" for page in reader.pages)
    except Exception:
        raise HTTPException(status_code=400, detail="Could not read this PDF")
    return {"text": text.strip()[:50000]}
