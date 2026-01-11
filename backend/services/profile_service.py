"""
Profile service for fetching mentor and mentee profiles.

This service provides utilities for retrieving user profiles with their interests,
which are used by both the matching and request services.
"""
from typing import Optional
from uuid import UUID
from fastapi import HTTPException, status

from services.database import supabase
from models.mentor import MentorProfile
from models.mentee import MenteeProfile
from models.user import UserProfile
from models.interest import Interest


class ProfileService:
    """Service for fetching and managing user profiles."""

    @staticmethod
    async def get_mentee_profile(user_id: UUID) -> Optional[MenteeProfile]:
        """
        Fetch mentee profile with interests joined.

        Args:
            user_id: UUID of the user

        Returns:
            MenteeProfile or None if not found
        """
        try:
            # Query mentee profile with interests
            result = supabase.table('mentee_profiles')\
                .select('*, mentee_interests(interest:interests(*))')\
                .eq('user_id', str(user_id))\
                .single()\
                .execute()

            if not result.data:
                return None

            # Transform nested interests structure
            data = result.data
            interest_relations = data.get('mentee_interests', [])
            interests = [
                Interest(**item['interest'])
                for item in interest_relations
                if item.get('interest')
            ]

            # Remove the nested field and add flattened interests
            profile_data = {k: v for k, v in data.items() if k != 'mentee_interests'}
            profile_data['interests'] = interests

            return MenteeProfile(**profile_data)

        except Exception as e:
            # If record not found, return None
            if 'PGRST116' in str(e) or 'not found' in str(e).lower():
                return None
            raise

    @staticmethod
    async def get_mentor_profile(user_id: UUID) -> Optional[MentorProfile]:
        """
        Fetch mentor profile with interests joined.

        Args:
            user_id: UUID of the user

        Returns:
            MentorProfile or None if not found
        """
        try:
            # Query mentor profile with interests
            result = supabase.table('mentor_profiles')\
                .select('*, mentor_interests(interest:interests(*))')\
                .eq('user_id', str(user_id))\
                .single()\
                .execute()

            if not result.data:
                return None

            # Transform nested interests structure
            data = result.data
            interest_relations = data.get('mentor_interests', [])
            interests = [
                Interest(**item['interest'])
                for item in interest_relations
                if item.get('interest')
            ]

            # Remove the nested field and add flattened interests
            profile_data = {k: v for k, v in data.items() if k != 'mentor_interests'}
            profile_data['interests'] = interests

            return MentorProfile(**profile_data)

        except Exception as e:
            # If record not found, return None
            if 'PGRST116' in str(e) or 'not found' in str(e).lower():
                return None
            raise

    @staticmethod
    async def get_user_profile(user_id: UUID) -> Optional[UserProfile]:
        """
        Fetch base user profile.

        Args:
            user_id: UUID of the user

        Returns:
            UserProfile or None if not found
        """
        try:
            result = supabase.table('user_profiles')\
                .select('*')\
                .eq('id', str(user_id))\
                .single()\
                .execute()

            if not result.data:
                return None

            return UserProfile(**result.data)

        except Exception as e:
            # If record not found, return None
            if 'PGRST116' in str(e) or 'not found' in str(e).lower():
                return None
            raise

    @staticmethod
    async def verify_user_role(user_id: UUID, required_role: str) -> None:
        """
        Verify user has the required role.

        Args:
            user_id: UUID of the user
            required_role: Required role ('mentor', 'mentee', or 'both')

        Raises:
            HTTPException: 403 if user doesn't have required role
            HTTPException: 404 if user profile not found
        """
        user_profile = await ProfileService.get_user_profile(user_id)

        if not user_profile:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User profile not found"
            )

        # Check if user has the required role
        if required_role == 'both':
            # Special case: must have exactly 'both' role
            if user_profile.role != 'both':
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="User must have 'both' role"
                )
        elif user_profile.role != required_role and user_profile.role != 'both':
            # Normal case: must have required role OR 'both'
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"User does not have '{required_role}' role"
            )

