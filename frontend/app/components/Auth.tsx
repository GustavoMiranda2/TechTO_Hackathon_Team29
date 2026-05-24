import { useState } from "react";
import * as api from "../api";
import type { User } from "../types";

const SITUATIONS = [
  { value: "student", label: "Student" },
  { value: "recent_grad", label: "Recent graduate" },
  { value: "transition", label: "Professional in transition" },
  { value: "working", label: "Already working in tech" },
  { value: "new_career", label: "Seeking a new career" },
];

const EXPERIENCE = [
  { value: "beginner", label: "Beginner" },
  { value: "some", label: "Some experience" },
  { value: "experienced", label: "Experienced" },
];

export default function Auth({
  onAuthed,
  onGuest,
}: {
  onAuthed: (user: User) => void;
  onGuest: () => void;
}) {
  const [mode, setMode] = useState<"signup" | "login">("signup");
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [situation, setSituation] = useState("student");
  const [skills, setSkills] = useState("");
  const [interests, setInterests] = useState("");
  const [goals, setGoals] = useState("");
  const [experience, setExperience] = useState("beginner");
  const [desiredRoles, setDesiredRoles] = useState("");

  async function submit() {
    if (!username.trim() || !password.trim()) {
      setError("Username and password are required.");
      return;
    }
    setBusy(true);
    setError(null);
    try {
      const user =
        mode === "signup"
          ? await api.signup({
              username: username.trim(),
              password,
              situation,
              skills,
              interests,
              goals,
              experience_level: experience,
              desired_roles: desiredRoles,
            })
          : await api.login(username.trim(), password);
      onAuthed(user);
    } catch (e) {
      setError(e instanceof Error ? e.message : "Something went wrong.");
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className="card auth">
      <div className="auth-tabs">
        <button
          className={`auth-tab ${mode === "signup" ? "active" : ""}`}
          onClick={() => setMode("signup")}
        >
          Create account
        </button>
        <button
          className={`auth-tab ${mode === "login" ? "active" : ""}`}
          onClick={() => setMode("login")}
        >
          Log in
        </button>
      </div>

      {error && <div className="error-banner">{error}</div>}

      <input
        className="field"
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <input
        className="field"
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />

      {mode === "signup" && (
        <>
          <label className="field-label">Where are you right now?</label>
          <select
            className="field"
            value={situation}
            onChange={(e) => setSituation(e.target.value)}
          >
            {SITUATIONS.map((s) => (
              <option key={s.value} value={s.value}>
                {s.label}
              </option>
            ))}
          </select>

          <label className="field-label">Experience level</label>
          <select
            className="field"
            value={experience}
            onChange={(e) => setExperience(e.target.value)}
          >
            {EXPERIENCE.map((s) => (
              <option key={s.value} value={s.value}>
                {s.label}
              </option>
            ))}
          </select>

          <input
            className="field"
            placeholder="Skills (e.g., Python, SQL, React)"
            value={skills}
            onChange={(e) => setSkills(e.target.value)}
          />
          <input
            className="field"
            placeholder="Interests (e.g., data, automation, security)"
            value={interests}
            onChange={(e) => setInterests(e.target.value)}
          />
          <input
            className="field"
            placeholder="Your goals (e.g., land a first tech job)"
            value={goals}
            onChange={(e) => setGoals(e.target.value)}
          />
          <input
            className="field"
            placeholder="Roles you're curious about (optional)"
            value={desiredRoles}
            onChange={(e) => setDesiredRoles(e.target.value)}
          />
        </>
      )}

      <button className="btn" onClick={submit} disabled={busy}>
        {busy ? "Please wait…" : mode === "signup" ? "Create account" : "Log in"}
      </button>
      <button className="link-btn" onClick={onGuest}>
        Continue as guest instead
      </button>
    </div>
  );
}
