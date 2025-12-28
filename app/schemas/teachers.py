from pydantic import BaseModel


class TeacherCreate(BaseModel):
    name: str
    subject: str


class TeacherResponse(BaseModel):
    id: str
    name: str
    subject: str
