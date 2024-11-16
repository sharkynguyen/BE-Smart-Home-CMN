from pydantic import BaseModel
from typing import Optional

class AdviceModel(BaseModel):
    msg: str
    heart: float
    oxygen: float
    updated_time: str
