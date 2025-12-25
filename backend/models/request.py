from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from models.common import HelpType, RequestStatus


class MentorshipRequest(BaseModel):
    """Domain model matching mentorship_requests table."""
    id: UUID
    mentee_id: UUID
    mentor_id: UUID
    help_type: HelpType
    context: str  # Short context about the request
    key_questions: Optional[List[str]] = None  # Specific questions (optional)
    status: RequestStatus = RequestStatus.PENDING
    created_at: datetime
    responded_at: Optional[datetime] = None

