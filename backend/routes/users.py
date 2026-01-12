from fastapi import APIRouter, Depends
from uuid import UUID

from middleware.auth import get_current_user
from schemas.user import UserProfileUpdate, UserProfileResponse
from services.user import UserService

router = APIRouter()


@router.get("/me", response_model=UserProfileResponse)
async def get_my_user_profile(
    user_id: UUID = Depends(get_current_user)
):
    """Get current user's profile."""
    return UserService.get_user_profile(user_id)


@router.put("/me", response_model=UserProfileResponse)
async def update_user_profile(
    profile_data: UserProfileUpdate,
    user_id: UUID = Depends(get_current_user)
):
    """Update current user's profile."""
    return UserService.update_user_profile(user_id, profile_data)

