from enum import Enum


class HelpType(str, Enum):
    RESUME_REVIEW = "resume_review"
    MOCK_INTERVIEW = "mock_interview"
    CAREER_ADVICE = "career_advice"
    SOCIAL_ADVICE = "social_advice"


class RequestStatus(str, Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    DECLINED = "declined"

