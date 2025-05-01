from adapters.database import Database

from utils import settings

database = Database(
    settings.MYSQL_DSN  
)