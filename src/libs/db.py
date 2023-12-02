
from datetime import datetime
from database.models import BotMessage
from database.database import session_maker
from message.shemas import SMessage


def save_message_db(message: SMessage, status_code: int) -> None:

    with session_maker() as session:

        bot_message = BotMessage()
        bot_message.sender = message.sender
        bot_message.text = message.text
        bot_message.datetime_create = datetime.now()
        bot_message.status_code = status_code

        session.add(bot_message)
        session.commit()
