from fastapi import APIRouter, Depends, HTTPException, status
from uuid import UUID

from middleware.auth import get_current_user
from schemas.user import UserProfileUpdate, UserProfileResponse

router = APIRouter()


@router.get("/me", response_model=UserProfileResponse)
async def get_my_user_profile(
    user_id: UUID = Depends(get_current_user)
):
    """Get current user's profile."""
    # TODO: Import and call UserService.get_user_profile(user_id)
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="UserService not implemented yet"
    )


@router.put("/me", response_model=UserProfileResponse)
async def update_user_profile(
    profile_data: UserProfileUpdate,
    user_id: UUID = Depends(get_current_user)
):
    """Update current user's profile."""
    # TODO: Import and call UserService.update_user_profile(user_id, profile_data)
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="UserService not implemented yet"
    )

