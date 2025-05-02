import uvicorn

from contextlib import asynccontextmanager

from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles

from utils import settings

from state import services

from web.api import api_router
from web import web_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await services.database.connect()
    yield
    await services.database.disconnect()

app = FastAPI(lifespan=lifespan)

app.include_router(api_router)
app.include_router(web_router)

app.mount("/static", StaticFiles(directory="src/web/static/"), name="static")
    
if __name__ == "__main__":
    uvicorn.run(
        "mizu:app",
        host=settings.MIZU_HOST,
        port=settings.MIZU_PORT,
        workers=settings.MIZU_WORKERS
    )
