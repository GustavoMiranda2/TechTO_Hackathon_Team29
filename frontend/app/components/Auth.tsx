import { useState } from "react";
import * as api from "../api";
import type { User } from "../types";

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
          ? await api.signup({ username: username.trim(), password })
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

      <button className="btn" onClick={submit} disabled={busy}>
        {busy ? "Please wait..." : mode === "signup" ? "Create account" : "Log in"}
      </button>
      <button className="link-btn" onClick={onGuest}>
        Continue as guest instead
      </button>
    </div>
  );
}
