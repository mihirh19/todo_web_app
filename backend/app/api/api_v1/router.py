from fastapi import APIRouter
from .handlers import user
from ..auth.jwt import auth_router
router = APIRouter()

router.include_router(user.user_router, prefix='/users', tags=['users'])
router.include_router(auth_router, prefix='/auth', tags=['auth'])

