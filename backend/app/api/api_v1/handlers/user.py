from fastapi import APIRouter, HTTPException, status
from ....schemas import UserAuth, UserOut
from ....services import UserService
import pymongo

user_router = APIRouter()


@user_router.post('/create', summary="create new user", response_model=UserOut)
async def create_user(data: UserAuth):
    try:
        return await UserService.create_user(data)
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='user will this email or username already exits')
