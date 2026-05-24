from __future__ import annotations

import json
import os

import requests
from anthropic import Anthropic
from roadmaps import get_roadmap, list_paths_for_prompt

ANTHROPIC_MODEL = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-6")

BACKBOARD_API_KEY = os.getenv("BACKBOARD_API_KEY")
BACKBOARD_PROVIDER = os.getenv("BACKBOARD_PROVIDER", "openai")
BACKBOARD_MODEL = os.getenv("BACKBOARD_MODEL", "gpt-4o")
BACKBOARD_URL = "https://app.backboard.io/api/threads/messages"

USE_BACKBOARD = bool(BACKBOARD_API_KEY)

anthropic_client = None if USE_BACKBOARD else Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def _complete(
    system: str,
    messages: list[dict],
    max_tokens: int = 2048,
    assistant_id: str | None = None,
    memory: str | None = None,
) -> tuple[str, str | None]:
    if USE_BACKBOARD:
        convo = "\n\n".join(f"{m['role'].upper()}: {m['content']}" for m in messages)
        content = (
            f"{system}\n\n=== CONVERSATION ===\n{convo}\n\n"
            "Return only the JSON described above, with no extra text."
        )
        payload = {
            "content": content,
            "llm_provider": BACKBOARD_PROVIDER,
            "model_name": BACKBOARD_MODEL,
            "stream": False,
        }
        if assistant_id:
            payload["assistant_id"] = assistant_id
        if memory:
            payload["memory"] = memory
        resp = requests.post(
            BACKBOARD_URL,
            json=payload,
            headers={"X-API-Key": BACKBOARD_API_KEY, "Content-Type": "application/json"},
            timeout=90,
        )
        resp.raise_for_status()
        data = resp.json()
        if data.get("status") != "COMPLETED":
            raise RuntimeError(data.get("content", "Backboard request failed"))
        return data["content"], data.get("assistant_id")
    if not os.getenv("ANTHROPIC_API_KEY"):
        raise RuntimeError(
            "AI provider key is not configured. Set BACKBOARD_API_KEY or ANTHROPIC_API_KEY in backend/.env."
        )
    response = anthropic_client.messages.create(
        model=ANTHROPIC_MODEL,
        max_tokens=max_tokens,
        system=system,
        messages=messages,
    )
    return response.content[0].text, None

SITUATION_GUIDANCE = {
    "student": (
        "This person is STILL STUDYING or just entering tech. Assume they may not know "
        "much yet. Keep questions simple, check whether programming basics feel exciting "
        "or frustrating, and guide them toward foundations such as programming logic, "
        "problem solving, basic web, data, security, or support before narrowing too hard."
    ),
    "recent_grad": (
        "This person HAS GRADUATED or is close to graduation. Assume they know some tech "
        "and may already know what they like, but still need help choosing a career "
        "direction. Ask about projects, classes, tools, tradeoffs, work style, and the "
        "kind of role they can picture occupying."
    ),
    "transition": (
        "This person is a PROFESSIONAL IN TRANSITION moving toward a new area of tech. "
        "Acknowledge their existing strengths and focus on which adjacent direction best "
        "uses what they already have while moving them where they want to go."
    ),
    "working": (
        "This person ALREADY WORKS IN TECH and wants to grow, specialize, or level up. "
        "Skip the basics; ask what they want to deepen, what they are bored of, and which "
        "direction would be a meaningful step up from where they are now."
    ),
    "new_career": (
        "This person is coming from OUTSIDE TECH and exploring a brand-new career. Be "
        "encouraging and concrete: connect their existing life or work strengths to tech "
        "directions, and keep jargon minimal."
    ),
}

SITUATION_ALIAS = {"graduated": "recent_grad"}

RETURNING_NOTE = (
    "This is a RETURNING user you have helped before. Do NOT re-ask the basic discovery "
    "questions you already know from their profile or previous questionnaire below. Greet "
    "them warmly, acknowledge you remember the last direction, then ask how it went and "
    "what changed: what they disliked, what they liked, new skills learned, shifted goals, "
    "or curiosity about a different area. Use old answers plus new answers for the next "
    "recommendation. Keep it short."
)

PROFILE_LABELS = [
    ("situation", "Situation"),
    ("experience_level", "Experience level"),
    ("skills", "Skills"),
    ("interests", "Interests"),
    ("goals", "Goals"),
    ("desired_roles", "Desired roles"),
    ("last_summary", "Last time we concluded"),
]


def _situation_note(situation: str) -> str:
    key = SITUATION_ALIAS.get(situation, situation)
    return SITUATION_GUIDANCE.get(key, SITUATION_GUIDANCE["recent_grad"])


def _profile_block(profile: dict | None) -> str:
    if not profile:
        return ""
    lines = []
    for key, label in PROFILE_LABELS:
        value = (profile.get(key) or "").strip()
        if value:
            lines.append(f"- {label}: {value}")
    if not lines:
        return ""
    return "KNOWN PROFILE OF THIS PERSON:\n" + "\n".join(lines)


INTERVIEW_SYSTEM = """You are CareerCompass, a warm, direct, and understanding IT career \
guide. You help someone discover which tech direction fits them.

Your only job now is to interview them to discover WHAT THEY LOVE DOING, so you can later \
point them to a direction. You decide every question yourself and adapt to this person; \
never follow a fixed script and never recommend roles yet.

INTERNAL DISCOVERY SKILLS:
- situation: whether they are still studying, close to graduation, graduated, changing \
careers, or already working in tech
- familiarity: languages, tools, school subjects, projects, or concepts they have touched
- curiosity: what they are curious about, even if they have more than one curiosity
- energy: tasks they enjoy, tasks that drain them, and what kind of problems pull them in
- work style: solo or team, deep focus or variety, visual building, logic, data, security, \
automation, helping people, or infrastructure
- goals: what they want next, what they do not want, and what would make the path feel worth it
- student basics: whether programming logic, building tiny apps, debugging, and learning \
fundamentals feel interesting enough to keep exploring
- graduate direction: which role families fit their projects, preferences, strengths, and \
market-readiness

Use these skills silently as the questionnaire targets. You must collect enough signal to \
answer them by the end, but do not ask these items as a checklist and do not expose this \
list to the user.

How to ask:
- ONE short question per turn. Keep every message under two sentences to respect their time.
- The person can choose more than one option. Remind them often that multiple answers are \
welcome, especially when asking about languages, tools, interests, or goals.
- Make each question concrete by giving 3-4 example answers in parentheses, so they know \
what kind of thing they can say. Example: "What kind of work pulls you in most? (e.g., \
building things people use, digging into data, automating boring tasks, breaking and \
securing systems)"
- React to their last answer in a few words, then ask the next thing.
- If an answer is vague, ask a sharper follow-up so you truly understand what they mean.

Uncover over about 5-6 short exchanges:
- what they enjoy doing most and what drains them
- whether they lean toward building, analyzing, securing, automating, or helping
- tools or languages they liked touching
- solo vs team, deep focus vs variety
- what they do NOT want
- for students: whether they should first explore programming logic, fundamentals, and tiny \
beginner projects before choosing a role
- for graduates: which career family is realistic and attractive enough to explore now

When you have enough signal, set "done" to true and make the final message ONE short \
sentence (e.g., "Got it, I have enough to find your direction."). Never summarize the \
conversation; long output wastes tokens.

Respond ONLY with valid JSON, no prose outside it:
{"message": "your next message to the user", "done": false}"""


DIAGNOSE_SYSTEM = """You are CareerCompass, an expert IT career consultant.

You receive an interview transcript and optionally a resume. Your job is NOT to grade \
the person on the experience they already have. Your job is to help them SEE WHO THEY \
COULD BECOME: which IT role they would naturally grow into and occupy, based on what \
energizes them, how they think, and what they enjoy. Think potential and direction, \
not a resume audit. The resume is only a secondary clue, mainly to spot misalignment.

The score reflects how well a path fits WHO THIS PERSON IS and could become, not how \
ready their current resume looks. Be specific and inspiring but honest, never generic.

Available career paths (use these exact keys):
{paths}

Respond ONLY with valid JSON in this exact shape:
{{
  "summary": "2-3 sentence vision of who this person could become and the direction that fits them",
  "inferred_profile": {{
    "situation": "student | recent_grad | transition | working | new_career",
    "experience_level": "beginner | some | experienced",
    "skills": "comma-separated languages, tools, subjects, concepts, or strengths they mentioned",
    "interests": "comma-separated areas, activities, and problems they seem drawn to",
    "goals": "short plain-English summary of what they want next",
    "desired_roles": "comma-separated career directions or role families that fit the diagnosis"
  }},
  "matches": [
    {{
      "key": "one of the path keys",
      "title": "human title",
      "score": 0-100,
      "role_overview": "what this role generally does, in plain language",
      "why": "why this person could thrive and grow into this role, referencing their own words",
      "difficulty": "Reachable now | Needs some prep | Aspirational",
      "market_note": "a short general note on employability or competition, without salary claims or pretending to use live market data",
      "have": ["strengths or interests that already point them toward this path"],
      "missing": ["what they would grow into or learn to occupy this role"],
      "day_in_life": "a vivid 2-3 sentence Tuesday in this role, so they can picture being there"
    }}
  ],
  "misalignment": {{
    "detected": true or false,
    "background_points_to": "where their past or resume leans, or null",
    "spark_points_to": "where their real energy and curiosity point, or null",
    "explanation": "gently explain that their past does not have to define their future, or empty string",
    "recommended_focus": "what direction they should explore to move toward who they could become"
  }}
}}

This is about guiding someone to discover an occupation they could love, never about \
finding a job opening or applying. Never mention recruiters, applications, or vacancies.
If the person is a student or very new, include at least one path whose first step is \
programming logic, fundamentals, and a tiny beginner project before specialization.
Return 3 matches, ordered by score descending."""


ROADMAP_SYSTEM = """You are CareerCompass, building a personalized 30-day study plan.

The person chose a career path. You are given the official roadmap.sh skill list for \
that path, plus the skills they already have. Do not invent skills outside the provided \
list except for small concrete actions (a project, a resume tweak). Skip what they \
already know so they do not waste time.

Respond ONLY with valid JSON in this exact shape:
{
  "path_title": "the role title",
  "roadmap_url": "the roadmap.sh url provided",
  "already_have": ["skills from the list they already master"],
  "to_learn": ["skills from the list they still need, in study order"],
  "weeks": [
    {"week": 1, "focus": "theme", "tasks": ["concrete task", "concrete task"]},
    {"week": 2, "focus": "theme", "tasks": ["..."]},
    {"week": 3, "focus": "theme", "tasks": ["..."]},
    {"week": 4, "focus": "theme", "tasks": ["..."]}
  ],
  "first_project": "one concrete portfolio project that fits this person and path"
}"""


def _extract_json(text: str) -> dict:
    text = text.strip()
    if text.startswith("```"):
        text = text.split("```", 2)[1]
        if text.startswith("json"):
            text = text[4:]
    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1:
        text = text[start : end + 1]
    return json.loads(text)


def interview_turn(
    history: list[dict],
    situation: str = "recent_grad",
    assistant_id: str | None = None,
    memory_on: bool = False,
    profile: dict | None = None,
    returning: bool = False,
) -> dict:
    system = f"{INTERVIEW_SYSTEM}\n\n{_situation_note(situation)}"
    block = _profile_block(profile)
    if block:
        system += f"\n\n{block}"
    if returning:
        system += f"\n\n{RETURNING_NOTE}"
    memory = "Auto" if memory_on else None
    text, aid = _complete(
        system, history, max_tokens=1024, assistant_id=assistant_id, memory=memory
    )
    result = _extract_json(text)
    result["assistant_id"] = aid
    return result


def diagnose(
    transcript: str,
    resume: str = "",
    situation: str = "recent_grad",
    assistant_id: str | None = None,
    memory_on: bool = False,
    profile: dict | None = None,
) -> dict:
    system = DIAGNOSE_SYSTEM.format(paths=list_paths_for_prompt())
    system = f"{system}\n\n{_situation_note(situation)}"
    block = _profile_block(profile)
    if block:
        system += f"\n\n{block}"
    user_content = f"INTERVIEW TRANSCRIPT:\n{transcript}\n\n"
    if resume.strip():
        user_content += f"RESUME:\n{resume}\n"
    else:
        user_content += "RESUME: (none provided)\n"
    memory = "Readonly" if memory_on else None
    text, _ = _complete(
        system,
        [{"role": "user", "content": user_content}],
        assistant_id=assistant_id,
        memory=memory,
    )
    return _extract_json(text)


def build_roadmap(path_key: str, have_skills: list[str], context: str = "") -> dict:
    roadmap = get_roadmap(path_key)
    if roadmap is None:
        raise ValueError(f"Unknown path: {path_key}")
    user_content = (
        f"PATH: {roadmap['title']}\n"
        f"ROADMAP URL: {roadmap['roadmap_url']}\n"
        f"OFFICIAL SKILL LIST: {', '.join(roadmap['skills'])}\n"
        f"SKILLS THEY ALREADY HAVE: {', '.join(have_skills) if have_skills else 'unknown'}\n"
        f"PERSON CONTEXT: {context or 'n/a'}\n"
    )
    text, _ = _complete(ROADMAP_SYSTEM, [{"role": "user", "content": user_content}])
    return _extract_json(text)
