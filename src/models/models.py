from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class User(BaseModel):
    user_id: int
    username: str
    created_at: Optional[datetime] = None

class APIKey(BaseModel):
    api_key: str
    user_id: int
    created_at: Optional[datetime] = None

