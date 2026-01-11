from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class TeacherCreate(BaseModel):
    name: str
    subject: str
    email: Optional[str] = None
    phone: Optional[str] = None


class TeacherResponse(BaseModel):
    id: str
    name: str
    subjects_ids: List[str]
    subjects_names: List[str] = []
    email: Optional[str] = None
    phone: Optional[str] = None
    is_active: bool
    created_at: datetime