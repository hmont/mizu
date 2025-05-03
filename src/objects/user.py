from typing import Optional
from typing import cast

from typing_extensions import TypedDict

from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy import delete as _delete

from models.user import UsersTable

from state.services import database

class User(TypedDict):
    id: int
    username: str
    password_hash: str
    openai_api_key: str

async def create(
    username: str,
    password_hash: str,
    openai_api_key: str = ""
) -> None:
    query = insert(UsersTable).values(
        username=username,
        password_hash=password_hash,
        openai_api_key=openai_api_key
    )

    await database.execute(query)

async def fetch_one(
    id: Optional[int] = None,
    username: Optional[str] = None
) -> Optional[User]:
    if not any((id, username)):
        raise ValueError("Either id or username must be provided.")

    stmt = select(UsersTable)

    if id:
        stmt = stmt.where(UsersTable.id == id)
    else:
        stmt = stmt.where(UsersTable.username == username)

    user = await database.fetch_one(stmt)

    return cast(User, user) if user is not None else None

async def delete(
    id: Optional[int] = None,
    username: Optional[str] = None
) -> int:
    if not any((id, username)):
        raise ValueError("Either id or username must be provided.")

    stmt = _delete(UsersTable)

    if id:
        stmt = stmt.where(UsersTable.id == id)
    else:
        stmt = stmt.where(UsersTable.username == username)

    return await database.execute(stmt)