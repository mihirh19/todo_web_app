from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from ...services.user_services import UserService
from ...core.security import create_refresh_token, create_access_token

auth_router = APIRouter()


@auth_router.post('/login')
async def login(form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    user = await UserService.authenticate(email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="incorrect email or password")

    # create a access and refresh token
    return {
        "access_token" : create_access_token(user.user_id),
        "refresh_token" : create_refresh_token(user.user_id)
    }
