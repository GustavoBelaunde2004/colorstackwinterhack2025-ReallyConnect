from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from models.common import HelpType
from models.interest import Interest
from models.mentor import MentorProfile


class MentorProfileCreate(BaseModel):
    """Schema for creating a mentor profile."""
    industry: Optional[str] = None
    job_title: Optional[str] = None  # Job title/position (e.g., "Senior Software Engineer")
    help_types_offered: List[HelpType]
    max_requests_per_week: int
    interest_ids: List[UUID]  # List of interest IDs


class MentorProfileUpdate(BaseModel):
    """Schema for updating a mentor profile (all fields optional)."""
    industry: Optional[str] = None
    job_title: Optional[str] = None  # Job title/position (e.g., "Senior Software Engineer")
    help_types_offered: Optional[List[HelpType]] = None
    max_requests_per_week: Optional[int] = None
    interest_ids: Optional[List[UUID]] = None  # List of interest IDs
    is_active: Optional[bool] = None


class MentorProfileResponse(BaseModel):
    """Schema for mentor profile API response."""
    id: UUID
    user_id: UUID
    industry: Optional[str] = None
    job_title: Optional[str] = None  # Job title/position (e.g., "Senior Software Engineer")
    help_types_offered: List[HelpType]
    max_requests_per_week: int
    interests: List[Interest]  # Full Interest objects
    is_active: bool
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_model(cls, model: MentorProfile) -> "MentorProfileResponse":
        """Convert MentorProfile model to response schema."""
        return cls(**model.dict())

