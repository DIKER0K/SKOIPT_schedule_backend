from fastapi import APIRouter
from app.api.v1.endpoints import teachers, subjects

router = APIRouter()

router.include_router(teachers.router, prefix="/teachers", tags=["Teachers"])
router.include_router(subjects.router, prefix="/subject", tags=["Subjects"])