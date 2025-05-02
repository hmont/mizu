from fastapi import APIRouter

from .register import router as register_router
from .auth import router as auth_router

api_router = APIRouter(
    prefix="/api")

api_router.include_router(register_router)
api_router.include_router(auth_router)
