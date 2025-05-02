from fastapi.templating import Jinja2Templates

from redis.asyncio import Redis

from adapters.database import Database

from utils import settings

database = Database(
    settings.MYSQL_DSN  
)

redis = Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB,
    username=settings.REDIS_USER,
    password=settings.REDIS_PASS
)

templates = Jinja2Templates(directory="src/web/static/html")