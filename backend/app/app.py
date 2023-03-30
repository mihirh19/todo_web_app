from fastapi import FastAPI
from .core.config import settings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from .models.user_model import User
from .api.api_v1.router import router

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)


@app.on_event("startup")
async def app_init():
    """
        Initialize crucial application services
    """
    db_client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).fodolist
    await init_beanie(
        database=db_client,
        document_models=[
            User
        ]
    )

app.include_router(router, prefix=settings.API_V1_STR)