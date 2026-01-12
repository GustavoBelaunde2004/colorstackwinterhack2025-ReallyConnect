from fastapi import APIRouter, Query
from typing import List, Optional

from models.interest import Interest
from services.interest import InterestService

router = APIRouter()


@router.get("", response_model=List[Interest])
async def get_all_interests(
    category: Optional[str] = Query(None, description="Filter by interest category")
):
    """
    Get all available interests.
    
    Public endpoint - no authentication required.
    Returns master list of all interests for use in dropdowns/autocomplete.
    """
    return InterestService.get_all_interests(category)

