from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .core import settings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from .models import User, Todo
from .api.api_v1 import router

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]

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
            User,
            Todo
        ]
    )


app.include_router(router, prefix=settings.API_V1_STR)


@app.get('/')
def index():
    return {'message': "server is running", "documents": "http://localhost:8000/docs",
            "postman Documentation": "https://documenter.getpostman.com/view/22926184/2s93RUtBH8"}
