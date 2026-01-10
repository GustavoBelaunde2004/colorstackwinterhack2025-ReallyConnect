from fastapi import APIRouter, Depends, HTTPException, status, Query
from uuid import UUID
from typing import List, Optional

from middleware.auth import get_current_user
from schemas.mentor import MentorProfileCreate, MentorProfileUpdate, MentorProfileResponse
from models.mentor import MentorProfile
from models.common import HelpType

router = APIRouter()


@router.get("/me", response_model=MentorProfileResponse)
async def get_my_mentor_profile(
    user_id: UUID = Depends(get_current_user)
):
    """Get current user's mentor profile."""
    # TODO: Import and call MentorService.get_mentor_profile(user_id)
    # For now, raise NotImplementedError
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="MentorService not implemented yet"
    )


@router.post("/me", response_model=MentorProfileResponse, status_code=status.HTTP_201_CREATED)
async def create_mentor_profile(
    profile_data: MentorProfileCreate,
    user_id: UUID = Depends(get_current_user)
):
    """Create mentor profile for current user."""
    # TODO: Import and call MentorService.create_mentor_profile(user_id, profile_data)
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="MentorService not implemented yet"
    )


@router.put("/me", response_model=MentorProfileResponse)
async def update_mentor_profile(
    profile_data: MentorProfileUpdate,
    user_id: UUID = Depends(get_current_user)
):
    """Update current user's mentor profile."""
    # TODO: Import and call MentorService.update_mentor_profile(user_id, profile_data)
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="MentorService not implemented yet"
    )


@router.get("", response_model=List[MentorProfileResponse])
async def browse_mentors(
    help_type: Optional[HelpType] = Query(None, description="Filter by help type"),
    industry: Optional[str] = Query(None, description="Filter by industry"),
    limit: int = Query(20, ge=1, le=50, description="Number of mentors per page"),
    offset: int = Query(0, ge=0, description="Pagination offset"),
    user_id: UUID = Depends(get_current_user)
):
    """Browse all active mentors. Available to both mentors and mentees."""
    # TODO: Import and call MentorService.browse_mentors(user_id, help_type, industry, limit, offset)
    # Service should exclude mentors user already has pending/accepted requests with
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="MentorService not implemented yet"
    )


@router.get("/{mentor_id}", response_model=MentorProfileResponse)
async def get_mentor_profile(
    mentor_id: UUID,
    user_id: UUID = Depends(get_current_user)
):
    """Get public mentor profile by ID."""
    # TODO: Import and call MentorService.get_mentor_profile(mentor_id)
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="MentorService not implemented yet"
    )

