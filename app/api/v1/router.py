from fastapi import APIRouter
from app.api.v1.endpoints import teachers

router = APIRouter()

router.include_router(teachers.router, prefix="/teachers", tags=["Teachers"])