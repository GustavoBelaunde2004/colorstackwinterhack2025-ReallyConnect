from uuid import UUID
from fastapi import HTTPException, status
from datetime import datetime

from services.database import supabase
from models.user import UserProfile
from schemas.user import UserProfileUpdate, UserProfileResponse


class UserService:
    """Service for user profile operations."""
    
    @staticmethod
    def get_user_profile(user_id: UUID) -> UserProfileResponse:
        """Get user profile by ID."""
        try:
            result = supabase.table("user_profiles").select("*").eq("id", str(user_id)).execute()
            
            if not result.data:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="User profile not found"
                )
            
            data = result.data[0]
            user_profile = UserProfile(
                id=UUID(data["id"]),
                full_name=data.get("full_name"),
                role=data["role"],
                created_at=datetime.fromisoformat(data["created_at"].replace("Z", "+00:00")),
                updated_at=datetime.fromisoformat(data["updated_at"].replace("Z", "+00:00"))
            )
            
            return UserProfileResponse.from_model(user_profile)
            
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error fetching user profile: {str(e)}"
            )
    
    @staticmethod
    def update_user_profile(user_id: UUID, update_data: UserProfileUpdate) -> UserProfileResponse:
        """Update user profile."""
        try:
            # Build update dict from non-None values
            update_dict = {}
            if update_data.full_name is not None:
                update_dict["full_name"] = update_data.full_name
            if update_data.role is not None:
                update_dict["role"] = update_data.role
            
            if not update_dict:
                # No updates, return current profile
                return UserService.get_user_profile(user_id)
            
            update_dict["updated_at"] = datetime.utcnow().isoformat()
            
            result = supabase.table("user_profiles").update(update_dict).eq("id", str(user_id)).execute()
            
            if not result.data:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="User profile not found"
                )
            
            data = result.data[0]
            user_profile = UserProfile(
                id=UUID(data["id"]),
                full_name=data.get("full_name"),
                role=data["role"],
                created_at=datetime.fromisoformat(data["created_at"].replace("Z", "+00:00")),
                updated_at=datetime.fromisoformat(data["updated_at"].replace("Z", "+00:00"))
            )
            
            return UserProfileResponse.from_model(user_profile)
            
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error updating user profile: {str(e)}"
            )

