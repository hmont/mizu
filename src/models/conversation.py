from datetime import datetime

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy import String
from sqlalchemy import ForeignKey

from . import Base

class ConversationsTable(Base):
    __tablename__ = "conversations"
    
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    started_at: Mapped[datetime] = mapped_column(nullable=False, default=datetime.utcnow())
