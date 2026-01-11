from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class GroupCreate(BaseModel):
    name: str
    specialty: str
    year_start: int
    currator_id: Optional[str] = None
    student_count: Optional[int] = None
    
class GroupResponse(BaseModel):
    id: str
    name: str
    specialty: str
    year_start: int
    gradution_year: int
    currator_id: Optional[str] = None
    currator_name: Optional[str] = None
    student_count: Optional[int] = None
    is_active: bool
    created_at: datetime