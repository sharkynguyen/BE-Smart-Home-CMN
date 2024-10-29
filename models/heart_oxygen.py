from pydantic import BaseModel
from datetime import datetime
now = datetime.now()

class HeartOxyGen(BaseModel):
    name: str
    description: str
    heart: int
    oxygen: int
    updated_time: str

