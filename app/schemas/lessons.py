from typing import List, Optional
from pydantic import BaseModel
from datetime import date, datetime, time

class LessonCreate(BaseModel):
    subject_id: str
    teacher_ids: List[str]
    date: date
    start_time: time
    classroom: Optional[str] = None
    
class LessonResponse(BaseModel):
    id: str
    subject_id: str
    subject_name: str
    teacher_ids: List[str]
    teacher_names: List[str]
    date: date
    start_time: time
    end_time: time
    duration_hours: float
    classroom: Optional[str] = None
    is_canceled: bool = False
    created_at: datetime