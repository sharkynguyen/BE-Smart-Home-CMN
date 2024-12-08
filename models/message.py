from pydantic import BaseModel
from datetime import datetime


class MessageModel(BaseModel):
    role: int
    message: str
    updated_time: str
