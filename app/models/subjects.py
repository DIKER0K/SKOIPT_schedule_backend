from pydantic import BaseModel, Field
from bson import ObjectId

class SubjectDB(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    name: str
    required_hours: int
    max_hours: int
    self_study_hours: int
    exam_consultation_hours: int
    exam_hours: int
    has_exam: bool
    
    class Config:
        arbitrary_types_allowed = True