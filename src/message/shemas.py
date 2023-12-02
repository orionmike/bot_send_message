from pydantic import BaseModel


class SMessage(BaseModel):
    sender: str
    text: str
