from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from models.common import HelpType
from models.mentor import MentorProfile


class MentorProfileCreate(BaseModel):
    """Schema for creating a mentor profile."""
    industry: Optional[str] = None
    role: Optional[str] = None
    help_types_offered: List[HelpType]
    max_requests_per_week: int
    interests: List[str]


class MentorProfileUpdate(BaseModel):
    """Schema for updating a mentor profile (all fields optional)."""
    industry: Optional[str] = None
    role: Optional[str] = None
    help_types_offered: Optional[List[HelpType]] = None
    max_requests_per_week: Optional[int] = None
    interests: Optional[List[str]] = None
    is_active: Optional[bool] = None


class MentorProfileResponse(BaseModel):
    """Schema for mentor profile API response."""
    id: UUID
    user_id: UUID
    industry: Optional[str] = None
    role: Optional[str] = None
    help_types_offered: List[HelpType]
    max_requests_per_week: int
    interests: List[str]
    is_active: bool
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_model(cls, model: MentorProfile) -> "MentorProfileResponse":
        """Convert MentorProfile model to response schema."""
        return cls(**model.dict())

