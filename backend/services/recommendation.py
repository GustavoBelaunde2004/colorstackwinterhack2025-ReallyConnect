from uuid import UUID
from typing import List, Optional
from fastapi import HTTPException, status

from services.database import supabase
from services.mentor import MentorService
from models.common import HelpType
from schemas.mentor import MentorProfileResponse


class RecommendationService:
    """Service for mentor recommendation operations."""
    
    @staticmethod
    def get_recommended_mentors(
        user_id: UUID,
        help_type: Optional[HelpType] = None,
        limit: int = 20,
        offset: int = 0
    ) -> List[MentorProfileResponse]:
        """
        Get recommended mentors for "For You" feed (mentees only).
        
        Returns personalized mentor recommendations based on mentee's profile,
        interests, and help needed. Uses simple interest matching algorithm.
        """
        try:
            # Verify user is a mentee
            mentee_profile = supabase.table("mentee_profiles").select("id, user_id").eq("user_id", str(user_id)).execute()
            if not mentee_profile.data:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Only mentees can get mentor recommendations"
                )
            
            mentee_id = mentee_profile.data[0]["id"]
            
            # Get mentee's interests
            mentee_interests_result = supabase.table("mentee_interests").select("interest_id").eq("mentee_profile_id", str(mentee_id)).execute()
            mentee_interest_ids = {UUID(row["interest_id"]) for row in mentee_interests_result.data}
            
            # Get mentors using browse_mentors (excludes existing connections/requests)
            mentors = MentorService.browse_mentors(user_id, help_type, None, limit * 2, offset)  # Get more to filter by interests
            
            # Score mentors by shared interests
            scored_mentors = []
            for mentor in mentors:
                mentor_interest_ids = {interest.id for interest in mentor.interests}
                shared_count = len(mentee_interest_ids & mentor_interest_ids)
                scored_mentors.append((shared_count, mentor))
            
            # Sort by shared interest count (descending), then by created_at
            scored_mentors.sort(key=lambda x: (x[0], x[1].created_at), reverse=True)
            
            # Return top mentors up to limit
            recommended = [mentor for _, mentor in scored_mentors[:limit]]
            
            return recommended
            
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error getting recommended mentors: {str(e)}"
            )

