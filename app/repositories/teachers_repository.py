from app.models.teachers import TeacherDB

class TeacherRepository:
    """
    Репозиторий = ТОЛЬКО доступ к данным
    """
    def __init__(self, db):
        self.collections = db["teachers"]

    async def create(self, teacher: TeacherDB) -> TeacherDB:
        await self.collections.insert_one(teacher.dict(by_alias=True))
        return teacher

    async def get_by_id(self, teacher_id):
        data = await self.collections.find_one({"_id": teacher_id})
        return TeacherDB(**data) if data else None