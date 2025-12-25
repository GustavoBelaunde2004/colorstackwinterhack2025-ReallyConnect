from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from models.common import HelpType, RequestStatus
from models.request import MentorshipRequest


class MentorshipRequestCreate(BaseModel):
    """Schema for creating a mentorship request."""
    mentor_id: UUID
    help_type: HelpType
    context: str  # Short context about the request
    key_questions: List[str]  # Specific questions


class MentorshipRequestResponse(BaseModel):
    """Schema for mentorship request API response."""
    id: UUID
    mentee_id: UUID
    mentor_id: UUID
    help_type: HelpType
    context: str
    key_questions: List[str]
    status: RequestStatus
    created_at: datetime
    responded_at: Optional[datetime] = None

    @classmethod
    def from_model(cls, model: MentorshipRequest) -> "MentorshipRequestResponse":
        """Convert MentorshipRequest model to response schema."""
        return cls(**model.dict())


class MentorshipRequestListResponse(BaseModel):
    """Schema for list of mentorship requests."""
    requests: List[MentorshipRequestResponse]
    total: int

