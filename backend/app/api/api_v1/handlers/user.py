from fastapi import APIRouter

user_router = APIRouter()


@user_router.post('/create', summary="create new user")
async def create_user(data):
    pass

