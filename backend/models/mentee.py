from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from models.common import HelpType
from models.interest import Interest


class MenteeProfile(BaseModel):
    """Domain model matching mentee_profiles table."""
    id: UUID
    user_id: UUID
    industry: Optional[str] = None
    goals: Optional[str] = None
    help_needed: List[HelpType]
    background: Optional[str] = None
    interests: List[Interest]
    profile_picture_url: Optional[str] = None
    created_at: datetime
    updated_at: datetime
