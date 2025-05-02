from datetime import datetime

from typing import Optional
from typing import TypedDict
from typing import cast

from sqlalchemy import insert
from sqlalchemy import select

from models.message import MessageTable

from state.services import database

class Message(TypedDict):
    id: int
    conversation_id: int
    sender: str
    content: str
    timestamp: datetime

async def create(
    conversation_id: Optional[int] = None,
    sender: str = "bot",
    content: str = "",
    timestamp: Optional[datetime] = None
) -> None:
    if not conversation_id:
        raise ValueError("Message must have conversation id")

    if not timestamp:
        timestamp = datetime.utcnow()

    stmt = insert(MessageTable).values(
        conversation_id=conversation_id,
        sender=sender,
        content=content,
        timestamp=timestamp
    )

    await database.execute(stmt)

async def fetch_one(
    _id: int
) -> Optional[Message]:
    query = select(MessageTable).where(MessageTable.id == _id)

    msg = await database.fetch_one(query)

    return cast(Message, msg) if msg else None