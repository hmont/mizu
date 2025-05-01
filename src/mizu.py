import asyncio

import time

from fastapi import FastAPI

from state.services import database

from sqlalchemy import select

from models import user

from objects.user import fetch_one, create, delete
from objects.conversation import create as convocreate, fetch_one as convofetch
from objects.message import create as createmsg

async def main():
    await database.connect()
    await create("henry3", "a", "b")
    await convocreate(1)
    
    # the = await delete(username="henry3")
    # print(the)
    
    # the = await convofetch(1)
    
    await createmsg(conversation_id=1)
    
    print()

if __name__ == "__main__":
    asyncio.run(main())
