from app.schemas.teachers import TeacherCreate
from app.models.teachers import TeacherDB
from app.repositories.teachers_repository import TeacherRepository


class TeacherService:
    """
    Сервис = правила и сценарии
    """

    def __init__(self, repo: TeacherRepository):
        self.repo = repo

    async def create_teacher(self, data: TeacherCreate) -> TeacherDB:
        teacher = TeacherDB(
            name=data.name,
            subject=data.subject,
        )
        return await self.repo.create(teacher)
