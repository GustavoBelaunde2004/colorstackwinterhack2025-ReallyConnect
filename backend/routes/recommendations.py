from fastapi import APIRouter, Depends, Query
from uuid import UUID
from typing import List, Optional

from middleware.auth import get_current_user
from schemas.mentor import MentorProfileResponse
from models.common import HelpType
from services.recommendation import RecommendationService

router = APIRouter()


@router.get("", response_model=List[MentorProfileResponse])
async def get_recommended_mentors(
    help_type: Optional[HelpType] = Query(None, description="Filter by help type"),
    limit: int = Query(20, ge=1, le=50, description="Number of recommended mentors"),
    offset: int = Query(0, ge=0, description="Pagination offset"),
    user_id: UUID = Depends(get_current_user)
):
    """
    Get recommended mentors for "For You" feed (mentees only).
    
    Returns personalized mentor recommendations based on mentee's profile,
    interests, and help needed. This is the swipeable feed for mentees.
    """
    return RecommendationService.get_recommended_mentors(user_id, help_type, limit, offset)



