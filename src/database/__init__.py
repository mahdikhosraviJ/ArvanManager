# database.py
import sqlite3
from contextlib import contextmanager
from typing import Optional
from src.models import User, APIKey

class Database:
    def __init__(self, db_file="bot_database.db"):
        self.db_file = db_file
        self._create_tables()

    @contextmanager
    def get_connection(self):
        conn = sqlite3.connect(self.db_file)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
        finally:
            conn.close()

    def _create_tables(self):
        with self.get_connection() as conn:
            conn.executescript("""
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                CREATE TABLE IF NOT EXISTS api_keys (
                    api_key TEXT PRIMARY KEY,
                    user_id INTEGER,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY(user_id) REFERENCES users(user_id)
                );
            """)

    def add_user(self, user: User):
        with self.get_connection() as conn:
            conn.execute("INSERT INTO users (user_id, username) VALUES (?, ?)", (user.user_id, user.username))

    def get_user(self, user_id: int) -> Optional[User]:
        with self.get_connection() as conn:
            row = conn.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone()
            if row:
                return User(**dict(row))
            return None

    def add_api_key(self, api_key: APIKey):
        with self.get_connection() as conn:
            conn.execute("INSERT INTO api_keys (api_key, user_id) VALUES (?, ?)", (api_key.api_key, api_key.user_id))

    def get_api_key(self, api_key: str) -> Optional[APIKey]:
        with self.get_connection() as conn:
            row = conn.execute("SELECT * FROM api_keys WHERE api_key = ?", (api_key,)).fetchone()
            if row:
                return APIKey(**dict(row))
            return None

    def get_user_api_keys(self, user_id: int) -> list[APIKey]:
        with self.get_connection() as conn:
            rows = conn.execute("SELECT * FROM api_keys WHERE user_id = ?", (user_id,)).fetchall()
            return [APIKey(**dict(row)) for row in rows]

    def delete_user(self, user_id: int):
        with self.get_connection() as conn:
            conn.execute("DELETE FROM users WHERE user_id = ?", (user_id,))

    def delete_api_key(self, api_key: str):
        with self.get_connection() as conn:
            conn.execute("DELETE FROM api_keys WHERE api_key = ?", (api_key,))

    def delete_user_api_keys(self, user_id: int):
        with self.get_connection() as conn:
            conn.execute("DELETE FROM api_keys WHERE user_id = ?", (user_id,))