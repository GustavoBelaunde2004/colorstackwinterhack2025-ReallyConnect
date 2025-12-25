from fastapi import APIRouter, Depends, HTTPException, status
from uuid import UUID

from middleware.auth import get_current_user
from schemas.request import (
    MentorshipRequestCreate,
    MentorshipRequestResponse,
    MentorshipRequestListResponse
)

router = APIRouter()


@router.post("", response_model=MentorshipRequestResponse, status_code=status.HTTP_201_CREATED)
async def create_mentorship_request(
    request_data: MentorshipRequestCreate,
    user_id: UUID = Depends(get_current_user)
):
    """Create a mentorship request (mentee only)."""
    # TODO: Import and call RequestService.create_request(user_id, request_data)
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="RequestService not implemented yet"
    )


@router.get("", response_model=MentorshipRequestListResponse)
async def get_my_requests(
    user_id: UUID = Depends(get_current_user)
):
    """Get user's mentorship requests (different for mentors vs mentees)."""
    # TODO: Import and call RequestService.get_requests_for_user(user_id)
    # Service should determine if user is mentor or mentee and return appropriate requests
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="RequestService not implemented yet"
    )


@router.get("/{request_id}", response_model=MentorshipRequestResponse)
async def get_request(
    request_id: UUID,
    user_id: UUID = Depends(get_current_user)
):
    """Get specific mentorship request (must be involved as mentor or mentee)."""
    # TODO: Import and call RequestService.get_request(request_id, user_id)
    # Service should verify user has access to this request
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="RequestService not implemented yet"
    )


@router.patch("/{request_id}/accept", response_model=MentorshipRequestResponse)
async def accept_request(
    request_id: UUID,
    user_id: UUID = Depends(get_current_user)
):
    """Accept a mentorship request (mentor only)."""
    # TODO: Import and call RequestService.accept_request(request_id, user_id)
    # Service should verify user is the mentor for this request
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="RequestService not implemented yet"
    )


@router.patch("/{request_id}/decline", response_model=MentorshipRequestResponse)
async def decline_request(
    request_id: UUID,
    user_id: UUID = Depends(get_current_user)
):
    """Decline a mentorship request (mentor only)."""
    # TODO: Import and call RequestService.decline_request(request_id, user_id)
    # Service should verify user is the mentor for this request
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="RequestService not implemented yet"
    )

