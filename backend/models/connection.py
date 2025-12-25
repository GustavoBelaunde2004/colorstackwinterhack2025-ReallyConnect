from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class Connection(BaseModel):
    """Domain model matching connections table."""
    id: UUID
    mentor_id: UUID
    mentee_id: UUID
    request_id: Optional[UUID] = None  # Links to original request
    created_at: datetime

