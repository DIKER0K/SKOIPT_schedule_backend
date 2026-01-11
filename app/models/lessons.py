from typing import List, Optional
from bson import ObjectId
from pydantic import BaseModel, Field
from datetime import datetime
from app.utils.datetime import now


class LessonDB(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    subject_id: ObjectId
    teacher_ids: List[ObjectId] = Field(default_factory=list)
    date: datetime
    start_time: str
    end_time: str
    duration_hours: float
    classroom: Optional[str] = None
    is_canceled: bool = False
    created_at: datetime = Field(default_factory=now)
    
    class Config:
        arbitrary_types_allowed = True