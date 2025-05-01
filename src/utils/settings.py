import os

from dotenv import load_dotenv

load_dotenv(override=True)

MYSQL_HOST = str(os.environ['MYSQL_HOST'])
MYSQL_PORT = int(os.environ['MYSQL_PORT'])
MYSQL_USER = str(os.environ['MYSQL_USER'])
MYSQL_PASS = str(os.environ['MYSQL_PASS'])
MYSQL_DB   = str(os.environ['MYSQL_DB'])

MYSQL_DSN  = f"mysql://{MYSQL_USER}:{MYSQL_PASS}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"