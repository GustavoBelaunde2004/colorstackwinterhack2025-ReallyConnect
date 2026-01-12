from fastapi import APIRouter, Depends
from uuid import UUID

from middleware.auth import get_current_user
from schemas.ai import RequestRewriteRequest, RequestRewriteResponse
from services.ai import AIService

router = APIRouter()


@router.post("/rewrite-request", response_model=RequestRewriteResponse)
async def rewrite_request(
    request_data: RequestRewriteRequest,
    user_id: UUID = Depends(get_current_user)
):
    """Get AI-suggested rewrite of mentorship request text."""
    return AIService.rewrite_request(request_data.original_text, request_data.questions)

