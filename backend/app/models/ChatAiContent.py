from pydantic import BaseModel


class ChatContent(BaseModel):
    message: str
