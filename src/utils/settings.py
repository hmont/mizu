import os

from urllib.parse import quote

from dotenv import load_dotenv

load_dotenv(override=True)

MIZU_HOST = str(os.environ['MIZU_HOST'])
MIZU_PORT = int(os.environ['MIZU_PORT'])
MIZU_WORKERS = int(os.environ['MIZU_WORKERS'])

MYSQL_HOST = str(os.environ['MYSQL_HOST'])
MYSQL_PORT = int(os.environ['MYSQL_PORT'])
MYSQL_USER = str(os.environ['MYSQL_USER'])
MYSQL_PASS = str(os.environ['MYSQL_PASS'])
MYSQL_DB   = str(os.environ['MYSQL_DB'])

MYSQL_DSN  = f"mysql://{MYSQL_USER}:{MYSQL_PASS}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"

REDIS_HOST = str(os.environ["REDIS_HOST"])
REDIS_PORT = int(os.environ["REDIS_PORT"])
REDIS_USER = str(os.environ["REDIS_USER"])
REDIS_PASS = quote(os.environ["REDIS_PASS"])
REDIS_DB = int(os.environ["REDIS_DB"])

REDIS_AUTH_STRING = f"{REDIS_USER}:{REDIS_PASS}@" if REDIS_USER and REDIS_PASS else ""
REDIS_DSN = f"redis://{REDIS_AUTH_STRING}{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"
