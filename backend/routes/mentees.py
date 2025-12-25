from fastapi import APIRouter, Depends, HTTPException, status
from uuid import UUID

from middleware.auth import get_current_user
from schemas.mentee import MenteeProfileCreate, MenteeProfileUpdate, MenteeProfileResponse

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

