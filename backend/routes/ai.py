from fastapi import APIRouter, Depends, HTTPException, status
from uuid import UUID

from middleware.auth import get_current_user
from schemas.ai import RequestRewriteRequest, RequestRewriteResponse

router = APIRouter()


@router.post("/rewrite-request", response_model=RequestRewriteResponse)
async def rewrite_request(
    request_data: RequestRewriteRequest,
    user_id: UUID = Depends(get_current_user)
):
    """Get AI-suggested rewrite of mentorship request text."""
    # TODO: Import and call AIService.rewrite_request(request_data.original_text, request_data.questions)
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="AIService not implemented yet"
    )

