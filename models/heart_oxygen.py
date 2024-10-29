from pydantic import BaseModel
from datetime import datetime
now = datetime.now()

class HeartOxyGen(BaseModel):
    name: str
    description: str
    heart: float
    oxygen: float
    updated_time: str

