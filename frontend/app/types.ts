export type Stage = "graduated" | "student";

export type Situation =
  | "student"
  | "recent_grad"
  | "transition"
  | "working"
  | "new_career";

export type User = {
  id: number;
  username: string;
  token: string;
  situation: string;
  skills: string;
  interests: string;
  goals: string;
  experience_level: string;
  desired_roles: string;
  assistant_id: string | null;
  last_summary: string;
  visits: number;
};

export type ChatMessage = {
  role: "user" | "assistant";
  content: string;
};

export type Match = {
  key: string;
  title: string;
  score: number;
  role_overview?: string;
  why: string;
  difficulty: string;
  market_note?: string;
  have: string[];
  missing: string[];
  day_in_life: string;
};

export type Misalignment = {
  detected: boolean;
  background_points_to: string | null;
  spark_points_to: string | null;
  explanation: string;
  recommended_focus: string;
};

export type InferredProfile = {
  situation: string;
  skills: string;
  interests: string;
  goals: string;
  experience_level: string;
  desired_roles: string;
};

export type Diagnosis = {
  summary: string;
  inferred_profile?: InferredProfile;
  matches: Match[];
  misalignment: Misalignment;
};

export type SessionSummary = {
  id: number;
  summary: string;
  created_at: string;
};

export type SessionDetail = {
  id: number;
  summary: string;
  created_at: string;
  messages: ChatMessage[];
  diagnosis: Diagnosis;
};

export type Roadmap = {
  path_title: string;
  roadmap_url: string;
  already_have: string[];
  to_learn: string[];
  weeks: { week: number; focus: string; tasks: string[] }[];
  first_project: string;
};
