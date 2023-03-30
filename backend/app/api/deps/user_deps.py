from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from ...core.config import settings
from ...models.user_model import User
from jose import jwt
reuseble_oauth = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR1}/auth/login",
    scheme_name="JWT"
)

async def get_current_user(token:str = Depends(reuseble_oauth))->User:
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.ALGORITHM])
    finally:
        pass
