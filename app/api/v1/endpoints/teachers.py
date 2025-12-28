from fastapi import APIRouter, Depends

from app.db.database import get_db
from app.repositories.teachers_repository import TeacherRepository
from app.schemas.teachers import TeacherResponse, TeacherCreate
from app.services.teachers_service import TeacherService

router = APIRouter()

def get_teacher_service(db=Depends(get_db)) -> TeacherService:
    repo = TeacherRepository(db)
    return TeacherService(repo)

@router.post("/", response_model=TeacherResponse)
async def create_teacher(data: TeacherCreate, service: TeacherService = Depends(get_teacher_service)):
    teacher = await service.create_teacher(data)
    return TeacherResponse(id=str(teacher.id), name=teacher.name, subject=teacher.subject)