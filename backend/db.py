from __future__ import annotations

import hashlib
import hmac
import os
import secrets
import sqlite3
from typing import Optional

DB_PATH = os.path.join(os.path.dirname(__file__), "careercompass.db")

PROFILE_FIELDS = [
    "situation",
    "skills",
    "interests",
    "goals",
    "experience_level",
    "desired_roles",
]


def _connect() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with _connect() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                salt TEXT NOT NULL,
                token TEXT NOT NULL,
                situation TEXT DEFAULT '',
                skills TEXT DEFAULT '',
                interests TEXT DEFAULT '',
                goals TEXT DEFAULT '',
                experience_level TEXT DEFAULT '',
                desired_roles TEXT DEFAULT '',
                assistant_id TEXT,
                last_summary TEXT DEFAULT '',
                visits INTEGER DEFAULT 0,
                created_at TEXT DEFAULT (datetime('now'))
            )
            """
        )
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                summary TEXT DEFAULT '',
                messages_json TEXT DEFAULT '[]',
                diagnosis_json TEXT DEFAULT '{}',
                created_at TEXT DEFAULT (datetime('now'))
            )
            """
        )


def _hash(password: str, salt: str) -> str:
    return hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), 100_000).hex()


def _public(row: sqlite3.Row) -> dict:
    data = {k: row[k] for k in row.keys()}
    data.pop("password_hash", None)
    data.pop("salt", None)
    return data


def create_user(username: str, password: str, profile: Optional[dict] = None) -> Optional[dict]:
    salt = secrets.token_hex(8)
    token = secrets.token_hex(16)
    profile = profile or {}
    values = [profile.get(f, "") for f in PROFILE_FIELDS]
    try:
        with _connect() as conn:
            cur = conn.execute(
                f"""
                INSERT INTO users
                (username, password_hash, salt, token, {", ".join(PROFILE_FIELDS)}, visits)
                VALUES (?, ?, ?, ?, {", ".join("?" for _ in PROFILE_FIELDS)}, 0)
                """,
                [username, _hash(password, salt), salt, token, *values],
            )
            row = conn.execute(
                "SELECT * FROM users WHERE id = ?", (cur.lastrowid,)
            ).fetchone()
        return _public(row)
    except sqlite3.IntegrityError:
        return None


def authenticate(username: str, password: str) -> Optional[dict]:
    with _connect() as conn:
        row = conn.execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        ).fetchone()
    if row is None:
        return None
    if not hmac.compare_digest(_hash(password, row["salt"]), row["password_hash"]):
        return None
    return _public(row)


def get_user_by_token(token: str) -> Optional[dict]:
    if not token:
        return None
    with _connect() as conn:
        row = conn.execute(
            "SELECT * FROM users WHERE token = ?", (token,)
        ).fetchone()
    return _public(row) if row else None


def update_profile(user_id: int, profile: dict) -> None:
    sets = ", ".join(f"{f} = ?" for f in PROFILE_FIELDS)
    values = [profile.get(f, "") for f in PROFILE_FIELDS]
    with _connect() as conn:
        conn.execute(f"UPDATE users SET {sets} WHERE id = ?", [*values, user_id])


def save_inferred_profile(user_id: int, profile: dict) -> None:
    clean = {f: str(profile.get(f, "") or "")[:1000] for f in PROFILE_FIELDS}
    update_profile(user_id, clean)


def set_situation(user_id: int, situation: str) -> None:
    with _connect() as conn:
        conn.execute("UPDATE users SET situation = ? WHERE id = ?", (situation, user_id))


def set_assistant_id(user_id: int, assistant_id: str) -> None:
    with _connect() as conn:
        conn.execute(
            "UPDATE users SET assistant_id = ? WHERE id = ?", (assistant_id, user_id)
        )


def set_last_summary(user_id: int, summary: str) -> None:
    with _connect() as conn:
        conn.execute(
            "UPDATE users SET last_summary = ? WHERE id = ?", (summary, user_id)
        )


def increment_visits(user_id: int) -> int:
    with _connect() as conn:
        conn.execute("UPDATE users SET visits = visits + 1 WHERE id = ?", (user_id,))
        row = conn.execute(
            "SELECT visits FROM users WHERE id = ?", (user_id,)
        ).fetchone()
    return row["visits"] if row else 0


def save_session(
    user_id: int, summary: str, messages_json: str, diagnosis_json: str
) -> int:
    with _connect() as conn:
        cur = conn.execute(
            """
            INSERT INTO sessions (user_id, summary, messages_json, diagnosis_json)
            VALUES (?, ?, ?, ?)
            """,
            (user_id, summary, messages_json, diagnosis_json),
        )
        return cur.lastrowid


def list_sessions(user_id: int) -> list[dict]:
    with _connect() as conn:
        rows = conn.execute(
            """
            SELECT id, summary, created_at FROM sessions
            WHERE user_id = ? ORDER BY id DESC
            """,
            (user_id,),
        ).fetchall()
    return [{k: r[k] for k in r.keys()} for r in rows]


def get_session(user_id: int, session_id: int) -> Optional[dict]:
    with _connect() as conn:
        row = conn.execute(
            "SELECT * FROM sessions WHERE id = ? AND user_id = ?",
            (session_id, user_id),
        ).fetchone()
    return {k: row[k] for k in row.keys()} if row else None
