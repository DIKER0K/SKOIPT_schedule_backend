import datetime
from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, Field

from app.utils.datetime import now

class GroupDB(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    name: str
    specialty: str
    year_start: int
    currator_id: Optional[ObjectId] = None
    student_count: int = 0
    is_active: bool = True
    created_at: datetime = Field(default_factory=now)
    
    class Config:
        arbitrary_types_allowed = True