from fastapi import APIRouter

from web.pages import pages_router

web_router = APIRouter()

web_router.include_router(pages_router)
