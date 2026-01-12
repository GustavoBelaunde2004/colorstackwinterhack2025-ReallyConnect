from fastapi import APIRouter, Depends, status
from uuid import UUID

from middleware.auth import get_current_user
from schemas.request import (
    MentorshipRequestCreate,
    MentorshipRequestResponse,
    MentorshipRequestListResponse
)
from services.request import RequestService

router = APIRouter()


@router.post("", response_model=MentorshipRequestResponse, status_code=status.HTTP_201_CREATED)
async def create_mentorship_request(
    request_data: MentorshipRequestCreate,
    user_id: UUID = Depends(get_current_user)
):
    """Create a mentorship request (mentee only)."""
    return RequestService.create_request(user_id, request_data)


@router.get("", response_model=MentorshipRequestListResponse)
async def get_my_requests(
    user_id: UUID = Depends(get_current_user)
):
    """Get user's mentorship requests (different for mentors vs mentees)."""
    return RequestService.get_requests_for_user(user_id)


@router.get("/{request_id}", response_model=MentorshipRequestResponse)
async def get_request(
    request_id: UUID,
    user_id: UUID = Depends(get_current_user)
):
    """Get specific mentorship request (must be involved as mentor or mentee)."""
    return RequestService.get_request(request_id, user_id)


@router.patch("/{request_id}/accept", response_model=MentorshipRequestResponse)
async def accept_request(
    request_id: UUID,
    user_id: UUID = Depends(get_current_user)
):
    """Accept a mentorship request (mentor only)."""
    return RequestService.accept_request(request_id, user_id)


@router.patch("/{request_id}/decline", response_model=MentorshipRequestResponse)
async def decline_request(
    request_id: UUID,
    user_id: UUID = Depends(get_current_user)
):
    """Decline a mentorship request (mentor only)."""
    return RequestService.decline_request(request_id, user_id)

