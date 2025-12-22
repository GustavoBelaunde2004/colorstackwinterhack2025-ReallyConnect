from enum import Enum
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class HelpType(str, Enum):
    RESUME_REVIEW = "resume_review"
    MOCK_INTERVIEW = "mock_interview"
    CAREER_ADVICE = "career_advice"
    SOCIAL_ADVICE = "social_advice"


class RequestStatus(str, Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    DECLINED = "declined"


class MentorProfile(BaseModel):
    user_id: UUID
    industry: Optional[str] = None
    role: Optional[str] = None
    help_types_offered: List[HelpType]
    max_requests_per_week: int
    interests: List[str]
    is_active: bool = True


class MenteeProfile(BaseModel):
    user_id: UUID
    goals: Optional[str] = None
    help_needed: List[HelpType]
    background: Optional[str] = None
    interests: List[str]


class MentorshipRequest(BaseModel):
    id: UUID
    mentee_id: UUID
    mentor_id: UUID
    help_type: HelpType
    status: RequestStatus = RequestStatus.PENDING
    created_at: datetime

