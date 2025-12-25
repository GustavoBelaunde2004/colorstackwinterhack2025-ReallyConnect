from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from models.common import HelpType
from models.interest import Interest


class MentorProfile(BaseModel):
    """Domain model matching mentor_profiles table."""
    id: UUID
    user_id: UUID
    industry: Optional[str] = None
    job_title: Optional[str] = None  # Job title/position (e.g., "Senior Software Engineer")
    help_types_offered: List[HelpType]
    max_requests_per_week: int
    interests: List[Interest]
    is_active: bool = True
    created_at: datetime
    updated_at: datetime

