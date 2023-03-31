from fastapi import APIRouter
from .handlers import user_router, todo_router
from ..auth import auth_router

router = APIRouter()

router.include_router(user_router, prefix='/users', tags=['users'])
router.include_router(auth_router, prefix='/auth', tags=['auth'])
router.include_router(todo_router, prefix='/todo', tags=['todo'])

