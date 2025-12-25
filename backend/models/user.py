from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class UserProfile(BaseModel):
    """Domain model matching user_profiles table."""
    id: UUID
    full_name: Optional[str] = None
    role: str  # mentor, mentee, or both
    created_at: datetime
    updated_at: datetime

