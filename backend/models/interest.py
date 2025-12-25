from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class Interest(BaseModel):
    """Domain model matching interests table."""
    id: UUID
    name: str
    category: Optional[str] = None
    created_at: datetime

