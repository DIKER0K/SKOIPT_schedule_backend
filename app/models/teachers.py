from pydantic import BaseModel, Field
from bson import ObjectId
from datetime import datetime
from app.utils.datetime import now

class TeacherDB(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    name: str
    subject: str
    created_at: datetime = Field(default_factory=now)

    class Config:
        arbitrary_types_allowed = True