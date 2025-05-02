from fastapi import APIRouter

from .dashboard import router as dashboard_router

pages_router = APIRouter()

pages_router.include_router(dashboard_router)
