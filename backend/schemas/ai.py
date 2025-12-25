from typing import List
from pydantic import BaseModel


class RequestRewriteRequest(BaseModel):
    """Schema for AI request rewrite input."""
    original_text: str
    questions: List[str]


class RequestRewriteResponse(BaseModel):
    """Schema for AI request rewrite output."""
    original_text: str
    suggested_text: str
    explanation: str  # What was improved and why

