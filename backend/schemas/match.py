from typing import List, Optional
from pydantic import BaseModel
from uuid import UUID
from schemas.mentor import MentorProfileResponse


class MatchResult(BaseModel):
    """Schema for a single match result."""
    mentor: MentorProfileResponse
    match_score: float  # Score between 0 and 1
    explanation: str  # Human-readable explanation of why they match


class MatchListResponse(BaseModel):
    """Schema for list of matches."""
    matches: List[MatchResult]
    total: int


class MatchExplanationResponse(BaseModel):
    """Schema for detailed match explanation."""
    mentor_id: UUID
    explanation: str
    factors: List[str]  # List of matching factors (career alignment, help type match, etc.)

