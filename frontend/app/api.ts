import type {
  ChatMessage,
  Diagnosis,
  Roadmap,
  SessionDetail,
  SessionSummary,
  User,
} from "./types";

let authToken: string | null = null;

export function setToken(token: string | null) {
  authToken = token;
}

function headers(): Record<string, string> {
  const h: Record<string, string> = { "Content-Type": "application/json" };
  if (authToken) h["Authorization"] = `Bearer ${authToken}`;
  return h;
}

async function post<T>(path: string, body: unknown): Promise<T> {
  const res = await fetch(path, {
    method: "POST",
    headers: headers(),
    body: JSON.stringify(body),
  });
  if (!res.ok) {
    const detail = await res.json().catch(() => null);
    throw new Error(detail?.detail || `Request failed: ${res.status}`);
  }
  return res.json();
}

async function get<T>(path: string): Promise<T> {
  const res = await fetch(path, { headers: headers() });
  if (!res.ok) throw new Error(`Request failed: ${res.status}`);
  return res.json();
}

export type SignupPayload = {
  username: string;
  password: string;
  situation: string;
  skills: string;
  interests: string;
  goals: string;
  experience_level: string;
  desired_roles: string;
};

export function signup(payload: SignupPayload) {
  return post<User>("/api/auth/signup", payload);
}

export function login(username: string, password: string) {
  return post<User>("/api/auth/login", { username, password });
}

export async function me(token: string): Promise<User> {
  const res = await fetch("/api/me", {
    headers: { Authorization: `Bearer ${token}` },
  });
  if (!res.ok) throw new Error("Not authenticated");
  return res.json();
}

export function interview(history: ChatMessage[], stage: string) {
  return post<{ message: string; done: boolean; assistant_id: string | null }>(
    "/api/interview",
    { history, stage },
  );
}

export function diagnose(
  transcript: string,
  resume: string,
  stage: string,
  messages: ChatMessage[],
) {
  return post<Diagnosis>("/api/diagnose", { transcript, resume, stage, messages });
}

export function getSessions() {
  return get<SessionSummary[]>("/api/sessions");
}

export function getSession(id: number) {
  return get<SessionDetail>(`/api/sessions/${id}`);
}

export function buildRoadmap(
  path_key: string,
  have_skills: string[],
  context: string,
) {
  return post<Roadmap>("/api/roadmap", { path_key, have_skills, context });
}

export async function parseResume(file: File): Promise<string> {
  const form = new FormData();
  form.append("file", file);
  const res = await fetch("/api/parse-resume", { method: "POST", body: form });
  if (!res.ok) throw new Error("Resume parse failed");
  const data = await res.json();
  return data.text as string;
}
