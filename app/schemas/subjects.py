from pydantic import BaseModel

class SubjectCreate(BaseModel):
    name: str
    required_hours: int
    max_hours: int
    self_study_hours: int
    exam_consultation_hours: int
    exam_hours: int
    has_exam: bool
    
class SubjectResponse(BaseModel):
    id: str
    name: str
    max_hours: int
    self_study_hours: int
    exam_consultation_hours: int
    exam_hours: int
    has_exam: bool