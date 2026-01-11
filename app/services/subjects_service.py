from app.schemas.subjects import SubjectCreate
from app.models.subjects import SubjectDB
from app.repositories.subjects_repository import SubjectRepository

class SubjectService:
    def __init__(self, repo: SubjectRepository):
        self.repo = repo
        
    async def create_subject(self, data: SubjectCreate) -> SubjectDB:
        subject = SubjectDB(
            name = data.name,
            required_hours = data.required_hours,
            max_hours = data.max_hours,
            self_study_hours = data.self_study_hours,
            exam_consultation_hours = data.exam_consultation_hours,
            exam_hours = data.exam_hours,
            has_exam = data.has_exam
        )
        return await self.repo.create(subject)