from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from models.common import HelpType


class MenteeProfile(BaseModel):
    """Domain model matching mentee_profiles table."""
    id: UUID
    user_id: UUID
    goals: Optional[str] = None
    help_needed: List[HelpType]
    background: Optional[str] = None
    interests: List[str]
    created_at: datetime
    updated_at: datetime

