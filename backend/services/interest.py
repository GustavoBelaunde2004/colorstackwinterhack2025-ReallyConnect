from typing import List, Optional
from fastapi import HTTPException, status
from datetime import datetime
from uuid import UUID

from services.database import supabase
from models.interest import Interest


class InterestService:
    """Service for interest operations."""
    
    @staticmethod
    def get_all_interests(category: Optional[str] = None) -> List[Interest]:
        """Get all interests, optionally filtered by category."""
        try:
            query = supabase.table("interests").select("*")
            
            if category:
                query = query.eq("category", category)
            
            query = query.order("name")
            result = query.execute()
            
            interests = []
            for data in result.data:
                interest = Interest(
                    id=UUID(data["id"]),
                    name=data["name"],
                    category=data.get("category"),
                    created_at=datetime.fromisoformat(data["created_at"].replace("Z", "+00:00"))
                )
                interests.append(interest)
            
            return interests
            
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error fetching interests: {str(e)}"
            )
    
    @staticmethod
    def get_interests_by_ids(interest_ids: List[UUID]) -> List[Interest]:
        """Get interests by their IDs."""
        if not interest_ids:
            return []
        
        try:
            result = supabase.table("interests").select("*").in_("id", [str(id) for id in interest_ids]).execute()
            
            interests = []
            for data in result.data:
                interest = Interest(
                    id=UUID(data["id"]),
                    name=data["name"],
                    category=data.get("category"),
                    created_at=datetime.fromisoformat(data["created_at"].replace("Z", "+00:00"))
                )
                interests.append(interest)
            
            return interests
            
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error fetching interests: {str(e)}"
            )

