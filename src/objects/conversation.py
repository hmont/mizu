from datetime import datetime

from typing import TypedDict
from typing import Optional
from typing import cast

from sqlalchemy import insert
from sqlalchemy import select

from models.conversation import ConversationsTable

from state.services import database

from .user import User
    
class Conversation(TypedDict):
    id: int
    user_id: int
    started_at: datetime
    
    user: User
    messages: list
    
async def create(
    user_id: Optional[int] = None
) -> None:
    if not user_id:
        raise ValueError("user id must be provided")
    
    stmt = insert(ConversationsTable).values(
        user_id = user_id,
        started_at=datetime.utcnow())
    
    await database.execute(stmt)
    

async def fetch_one(
    id: Optional[int] = None
) -> Conversation:
    if not id:
        raise ValueError("id must be provided")
    
    stmt = select(ConversationsTable).where(ConversationsTable.id == id)
    
    conv = await database.fetch_one(stmt)
    
    return cast(Conversation, conv)