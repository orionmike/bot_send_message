from datetime import datetime
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column

from . database import Base


class BotMessage(Base):

    __tablename__ = 'bot_message'
    id: Mapped[int] = mapped_column(primary_key=True)
    sender: Mapped[str]
    text: Mapped[str]
    status_code: Mapped[Optional[int]]
    datetime_create: Mapped[datetime] = mapped_column(default=datetime.now())
