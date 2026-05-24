"use client";

import { useEffect, useRef, useState } from "react";
import * as api from "./api";
import type {
  ChatMessage,
  Diagnosis,
  Match,
  Roadmap,
  SessionSummary,
  Stage,
  User,
} from "./types";
import Auth from "./components/Auth";
import DiagnosisView from "./components/Diagnosis";
import RoadmapView from "./components/RoadmapView";

type Phase =
  | "welcome"
  | "auth"
  | "interview"
  | "resume"
  | "diagnosing"
  | "diagnosis"
  | "roadmap";

function errMsg(e: unknown): string {
  const base = e instanceof Error ? e.message : "Something went wrong";
  return `${base}. Check that the backend is running and the AI key is set.`;
}

export default function Home() {
  const [phase, setPhase] = useState<Phase>("welcome");
  const [user, setUser] = useState<User | null>(null);
  const [guestStage, setGuestStage] = useState<Stage>("student");
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState("");
  const [busy, setBusy] = useState(false);
  const [resume, setResume] = useState("");
  const [diagnosis, setDiagnosis] = useState<Diagnosis | null>(null);
  const [selected, setSelected] = useState<Match | null>(null);
  const [roadmap, setRoadmap] = useState<Roadmap | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [sessions, setSessions] = useState<SessionSummary[]>([]);
  const chatEnd = useRef<HTMLDivElement>(null);

  useEffect(() => {
    chatEnd.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, busy]);

  useEffect(() => {
    const token = localStorage.getItem("cc_token");
    if (!token) return;
    api.setToken(token);
    api
      .me(token)
      .then(setUser)
      .catch(() => {
        localStorage.removeItem("cc_token");
        api.setToken(null);
      });
  }, []);

  useEffect(() => {
    if (user && phase === "welcome") {
      api.getSessions().then(setSessions).catch(() => setSessions([]));
    }
  }, [user, phase]);

  function onAuthed(u: User) {
    localStorage.setItem("cc_token", u.token);
    api.setToken(u.token);
    setUser(u);
    setPhase("welcome");
  }

  async function openSession(id: number) {
    setError(null);
    try {
      const s = await api.getSession(id);
      setMessages(s.messages);
      setDiagnosis(s.diagnosis);
      setSelected(null);
      setRoadmap(null);
      setPhase("diagnosis");
    } catch (e) {
      setError(errMsg(e));
    }
  }

  function logout() {
    localStorage.removeItem("cc_token");
    api.setToken(null);
    setUser(null);
    reset();
  }

  function stageArg(): string {
    return user ? user.situation || "recent_grad" : guestStage;
  }

  async function begin() {
    setError(null);
    setMessages([]);
    setPhase("interview");
    setBusy(true);
    try {
      const res = await api.interview([], stageArg());
      setMessages([{ role: "assistant", content: res.message }]);
    } catch (e) {
      setError(errMsg(e));
    } finally {
      setBusy(false);
    }
  }

  function beginGuest(stage: Stage) {
    setGuestStage(stage);
    setError(null);
    setMessages([]);
    setPhase("interview");
    setBusy(true);
    api
      .interview([], stage)
      .then((res) =>
        setMessages([{ role: "assistant", content: res.message }]),
      )
      .catch((e) => setError(errMsg(e)))
      .finally(() => setBusy(false));
  }

  async function send() {
    const text = input.trim();
    if (!text || busy) return;
    const next: ChatMessage[] = [...messages, { role: "user", content: text }];
    setMessages(next);
    setInput("");
    setBusy(true);
    setError(null);
    try {
      const res = await api.interview(next, stageArg());
      setMessages([...next, { role: "assistant", content: res.message }]);
      if (res.done) setPhase("resume");
    } catch (e) {
      setError(errMsg(e));
    } finally {
      setBusy(false);
    }
  }

  async function onResumeFile(e: React.ChangeEvent<HTMLInputElement>) {
    const file = e.target.files?.[0];
    if (!file) return;
    setBusy(true);
    try {
      setResume(await api.parseResume(file));
    } finally {
      setBusy(false);
    }
  }

  async function runDiagnosis() {
    setError(null);
    setPhase("diagnosing");
    const transcript = messages
      .map((m) => `${m.role === "user" ? "User" : "CareerCompass"}: ${m.content}`)
      .join("\n");
    try {
      const data = await api.diagnose(transcript, resume, stageArg(), messages);
      setDiagnosis(data);
      setPhase("diagnosis");
    } catch (e) {
      setError(errMsg(e));
      setPhase("resume");
    }
  }

  async function pickPath(match: Match) {
    setSelected(match);
    setBusy(true);
    setError(null);
    try {
      const data = await api.buildRoadmap(
        match.key,
        match.have,
        diagnosis?.summary || "",
      );
      setRoadmap(data);
      setPhase("roadmap");
    } catch (e) {
      setError(errMsg(e));
    } finally {
      setBusy(false);
    }
  }

  function reset() {
    setPhase("welcome");
    setMessages([]);
    setResume("");
    setDiagnosis(null);
    setSelected(null);
    setRoadmap(null);
    setError(null);
  }

  const returning = Boolean(user?.last_summary);

  return (
    <div className="shell">
      <div className="brand">
        <div className="brand-dot" />
        <h1>CareerCompass AI</h1>
        {user && (
          <button className="link-btn brand-logout" onClick={logout}>
            Log out
          </button>
        )}
      </div>

      {error && <div className="error-banner">{error}</div>}

      {phase === "welcome" && (
        <div className="hero">
          {user ? (
            <>
              <h2>
                Welcome back,
                <br />
                <span className="grad">{user.username}</span>
              </h2>
              <p>
                {returning
                  ? "Let's check in on how your journey has evolved since last time."
                  : "Let's find the direction that fits you. I'll remember everything for next time."}
              </p>
              <button className="btn" onClick={begin}>
                {returning ? "Start a check-in" : "Start career diagnosis"}
              </button>
              {sessions.length > 0 && (
                <div className="history">
                  <div className="section-title">Your past sessions</div>
                  {sessions.map((s) => (
                    <button
                      key={s.id}
                      className="history-item"
                      onClick={() => openSession(s.id)}
                    >
                      <span className="history-date">
                        {s.created_at.slice(0, 10)}
                      </span>
                      <span className="history-summary">{s.summary}</span>
                    </button>
                  ))}
                </div>
              )}
            </>
          ) : (
            <>
              <h2>
                Don&apos;t search for jobs.
                <br />
                <span className="grad">Find where you fit.</span>
              </h2>
              <p>
                You already code a bit. The hard part is knowing which direction
                is yours. Let&apos;s figure that out together.
              </p>
              <button className="btn" onClick={() => setPhase("auth")}>
                Sign in / Create account
              </button>
              <div className="guest-divider">or continue as guest</div>
              <div className="stage-pick">
                <button
                  className="stage-card"
                  onClick={() => beginGuest("student")}
                >
                  <span className="stage-emoji">🎓</span>
                  <span className="stage-title">I&apos;m still studying</span>
                  <span className="stage-sub">
                    Find a direction to aim for
                  </span>
                </button>
                <button
                  className="stage-card"
                  onClick={() => beginGuest("graduated")}
                >
                  <span className="stage-emoji">🚀</span>
                  <span className="stage-title">I&apos;ve graduated</span>
                  <span className="stage-sub">
                    Find a role to step into now
                  </span>
                </button>
              </div>
            </>
          )}
        </div>
      )}

      {phase === "auth" && (
        <Auth onAuthed={onAuthed} onGuest={() => setPhase("welcome")} />
      )}

      {phase === "interview" && (
        <>
          <div className="chat">
            {messages.map((m, i) => (
              <div key={i} className={`bubble ${m.role === "user" ? "user" : "bot"}`}>
                {m.content}
              </div>
            ))}
            {busy && (
              <div className="typing">
                <span />
                <span />
                <span />
              </div>
            )}
            <div ref={chatEnd} />
          </div>
          <div className="composer">
            <textarea
              value={input}
              placeholder="Type your answer…"
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Enter" && !e.shiftKey) {
                  e.preventDefault();
                  send();
                }
              }}
            />
            <button className="btn" onClick={send} disabled={busy}>
              Send
            </button>
          </div>
        </>
      )}

      {phase === "resume" && (
        <div>
          <div className="section-title">One last thing (optional)</div>
          <div className="uploader">
            Drop your resume so I can spot the gap between what it says and what
            you actually want.
            <input type="file" accept="application/pdf" onChange={onResumeFile} />
          </div>
          {resume && (
            <div className="card" style={{ color: "var(--muted)", fontSize: 13 }}>
              Resume loaded ({resume.length} characters read).
            </div>
          )}
          <div className="row">
            <button className="btn" onClick={runDiagnosis} disabled={busy}>
              See my diagnosis
            </button>
          </div>
        </div>
      )}

      {phase === "diagnosing" && (
        <div className="hero">
          <div className="spinner" />
          <p>Reading everything you told me and finding your direction…</p>
        </div>
      )}

      {phase === "diagnosis" && diagnosis && (
        <div>
          <DiagnosisView
            data={diagnosis}
            selectedKey={selected?.key || null}
            onSelect={pickPath}
          />
          <p className="center" style={{ color: "var(--muted)", marginTop: 8 }}>
            {busy ? "Building your study plan…" : "Tap a path to get your study plan"}
          </p>
        </div>
      )}

      {phase === "roadmap" && roadmap && (
        <div>
          <RoadmapView data={roadmap} />
          <div className="row" style={{ marginTop: 16 }}>
            <button className="btn btn-ghost" onClick={() => setPhase("diagnosis")}>
              ← Back to my paths
            </button>
            <button className="btn btn-ghost" onClick={reset}>
              Start over
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
