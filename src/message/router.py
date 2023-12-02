
from fastapi import APIRouter

from config import TG_USER_ID
from libs.db import save_message_db
from libs.request import bot_send_message
from message.shemas import SMessage


router = APIRouter(prefix="/api/message", tags=["message"])


@router.post("/send")
async def send_message(message: SMessage):
    print(message)

    status_code = bot_send_message(TG_USER_ID, message.text)
    save_message_db(message, status_code)

    return {
        'status_code': status_code
    }
