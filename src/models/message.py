from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy import Enum
from sqlalchemy import Text
from sqlalchemy import DateTime
from sqlalchemy import Integer

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from . import Base

class MessageTable(Base):
    __tablename__ = 'messages'
    
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    conversation_id: Mapped[int] = mapped_column(ForeignKey("conversations.id"))
    sender = mapped_column(Enum("user", "bot"), name="sender")
    content: Mapped[str] = mapped_column(Text)
    timestamp: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow())