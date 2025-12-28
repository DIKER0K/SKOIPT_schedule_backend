from motor.motor_asyncio import AsyncIOMotorClient
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.v1.router import router as api_v1_router

from app.core.config import settings


@asynccontextmanager
async def lifespan(app:FastAPI):
    app.state.mongo_client = AsyncIOMotorClient(settings.MONGO_URI)
    app.state.db = app.state.mongo_client[settings.MONGO_DB]
    yield
    app.state.mongo_client.close()

app = FastAPI(title="Schedule backend", lifespan=lifespan)


app.include_router(api_v1_router, prefix="/api/v1")
