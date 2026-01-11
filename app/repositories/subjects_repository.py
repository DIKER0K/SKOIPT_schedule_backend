from app.models.subjects import SubjectDB

class SubjectRepository:
    def __init__(self, db):
        self.collections = db["subjects"]
        
    async def create(self, subject: SubjectDB) -> SubjectDB:
        await self.collections.insert_one(subject.dict(by_alias=True))
        return subject