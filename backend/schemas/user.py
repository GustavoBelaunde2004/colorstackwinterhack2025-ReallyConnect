from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from models.user import UserProfile


class UserProfileUpdate(BaseModel):
    """Schema for updating a user profile (all fields optional)."""
    full_name: Optional[str] = None
    role: Optional[str] = None  # mentor, mentee, or both


class UserProfileResponse(BaseModel):
    """Schema for user profile API response."""
    id: UUID
    full_name: Optional[str] = None
    role: str
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_model(cls, model: UserProfile) -> "UserProfileResponse":
        """Convert UserProfile model to response schema."""
        return cls(**model.dict())

