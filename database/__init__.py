import sqlite3
from contextlib import contextmanager

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

    def add_user(self, user_id, username):
        with self.get_connection() as conn:
            conn.execute("INSERT INTO users (user_id, username) VALUES (?, ?)", (user_id, username))
    def get_user(self, user_id):
        with self.get_connection() as conn:
            return conn.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone()
    def add_api_key(self, api_key, user_id):
        with self.get_connection() as conn:
            conn.execute("INSERT INTO api_keys (api_key, user_id) VALUES (?, ?)", (api_key, user_id))
    def get_api_key(self, api_key):
        with self.get_connection() as conn:
            return conn.execute("SELECT * FROM api_keys WHERE api_key = ?", (api_key,)).fetchone()
    def get_user_api_keys(self, user_id):
        with self.get_connection() as conn:
            return conn.execute("SELECT * FROM api_keys WHERE user_id = ?", (user_id,)).fetchall()
        
    def delete_user(self, user_id):
        with self.get_connection() as conn:
            conn.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
    
    def delete_api_key(self, api_key):
        with self.get_connection() as conn:
            conn.execute("DELETE FROM api_keys WHERE api_key = ?", (api_key,))

    def delete_user_api_keys(self, user_id):
        with self.get_connection() as conn:
            conn.execute("DELETE FROM api_keys WHERE user_id = ?", (user_id,))
        