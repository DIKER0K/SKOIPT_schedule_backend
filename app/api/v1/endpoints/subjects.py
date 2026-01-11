from fastapi import APIRouter, Depends

from app.db.database import get_db
from app.services.subjects_service import SubjectService
from app.repositories.subjects_repository import SubjectRepository
from app.schemas.subjects import SubjectCreate, SubjectResponse

router = APIRouter()

def get_subject_service (db=Depends(get_db)) -> SubjectService:
    repo = SubjectRepository(db)
    return SubjectService(repo)

@router.post("/", response_model=SubjectResponse)
async def create_subject(data: SubjectCreate, service: SubjectService = Depends(get_subject_service)):
    subject = await service.create_subject(data)
    return SubjectResponse(
                        id=str(subject.id), 
                        name=str(subject.name), 
                        max_hours=int(subject.max_hours), 
                        self_study_hours=int(subject.self_study_hours), 
                        exam_consultation_hours=int(subject.exam_consultation_hours), 
                        exam_hours=int(subject.exam_hours),
                        has_exam=bool(subject.has_exam)
                           )