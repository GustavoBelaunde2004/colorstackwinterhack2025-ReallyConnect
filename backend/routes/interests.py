from fastapi import APIRouter, Query, HTTPException, status
from typing import List, Optional

from models.interest import Interest

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
    # TODO: Import and call InterestService.get_all_interests(category)
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="InterestService not implemented yet"
    )

