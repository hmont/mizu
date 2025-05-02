from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from . import Base

class UsersTable(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    username: Mapped[str] = mapped_column(String(16), unique=True)
    password_hash: Mapped[str] = mapped_column(String(64))
    openai_api_key: Mapped[str] = mapped_column(String(64))
