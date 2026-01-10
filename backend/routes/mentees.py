from fastapi import APIRouter, Depends, HTTPException, status, Query
from uuid import UUID
from typing import List, Optional

from middleware.auth import get_current_user
from schemas.mentee import MenteeProfileCreate, MenteeProfileUpdate, MenteeProfileResponse
from models.common import HelpType

router = APIRouter()


@router.get("/me", response_model=MenteeProfileResponse)
async def get_my_mentee_profile(
    user_id: UUID = Depends(get_current_user)
):
    """Get current user's mentee profile."""
    # TODO: Import and call MenteeService.get_mentee_profile(user_id)
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="MenteeService not implemented yet"
    )


@router.post("/me", response_model=MenteeProfileResponse, status_code=status.HTTP_201_CREATED)
async def create_mentee_profile(
    profile_data: MenteeProfileCreate,
    user_id: UUID = Depends(get_current_user)
):
    """Create mentee profile for current user."""
    # TODO: Import and call MenteeService.create_mentee_profile(user_id, profile_data)
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="MenteeService not implemented yet"
    )


@router.put("/me", response_model=MenteeProfileResponse)
async def update_mentee_profile(
    profile_data: MenteeProfileUpdate,
    user_id: UUID = Depends(get_current_user)
):
    """Update current user's mentee profile."""
    # TODO: Import and call MenteeService.update_mentee_profile(user_id, profile_data)
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="MenteeService not implemented yet"
    )


@router.get("", response_model=List[MenteeProfileResponse])
async def browse_mentees(
    help_needed: Optional[HelpType] = Query(None, description="Filter by help type needed"),
    limit: int = Query(20, ge=1, le=50, description="Number of mentees per page"),
    offset: int = Query(0, ge=0, description="Pagination offset"),
    user_id: UUID = Depends(get_current_user)
):
    """Browse all mentees. Available to both mentors and mentees."""
    # TODO: Import and call MenteeService.browse_mentees(user_id, help_needed, limit, offset)
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="MenteeService not implemented yet"
    )


@router.get("/{mentee_id}", response_model=MenteeProfileResponse)
async def get_mentee_profile(
    mentee_id: UUID,
    user_id: UUID = Depends(get_current_user)
):
    """Get public mentee profile by ID."""
    # TODO: Import and call MenteeService.get_mentee_profile(mentee_id)
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="MenteeService not implemented yet"
    )

