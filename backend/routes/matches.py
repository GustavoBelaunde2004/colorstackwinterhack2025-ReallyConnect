from fastapi import APIRouter, Depends, HTTPException, status, Query
from uuid import UUID
from typing import Optional

from middleware.auth import get_current_user
from schemas.match import MatchListResponse, MatchExplanationResponse
from models.common import HelpType

router = APIRouter()


@router.get("", response_model=MatchListResponse)
async def get_matching_mentors(
    help_type: Optional[HelpType] = Query(None, description="Filter by help type"),
    limit: int = Query(10, ge=1, le=50, description="Maximum number of matches to return"),
    user_id: UUID = Depends(get_current_user)
):
    """Get matching mentors for current mentee."""
    # TODO: Import and call MatchingService.find_matching_mentors(user_id, help_type, limit)
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="MatchingService not implemented yet"
    )


@router.get("/{mentor_id}/explanation", response_model=MatchExplanationResponse)
async def get_match_explanation(
    mentor_id: UUID,
    user_id: UUID = Depends(get_current_user)
):
    """Get detailed explanation for why a mentor matches."""
    # TODO: Import and call MatchingService.get_match_explanation(user_id, mentor_id)
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="MatchingService not implemented yet"
    )

