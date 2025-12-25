from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from models.common import HelpType
from models.interest import Interest
from models.mentee import MenteeProfile


class MenteeProfileCreate(BaseModel):
    """Schema for creating a mentee profile."""
    goals: Optional[str] = None
    help_needed: List[HelpType]
    background: Optional[str] = None
    interest_ids: List[UUID]  # List of interest IDs


class MenteeProfileUpdate(BaseModel):
    """Schema for updating a mentee profile (all fields optional)."""
    goals: Optional[str] = None
    help_needed: Optional[List[HelpType]] = None
    background: Optional[str] = None
    interest_ids: Optional[List[UUID]] = None  # List of interest IDs


class MenteeProfileResponse(BaseModel):
    """Schema for mentee profile API response."""
    id: UUID
    user_id: UUID
    goals: Optional[str] = None
    help_needed: List[HelpType]
    background: Optional[str] = None
    interests: List[Interest]  # Full Interest objects
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_model(cls, model: MenteeProfile) -> "MenteeProfileResponse":
        """Convert MenteeProfile model to response schema."""
        return cls(**model.dict())

