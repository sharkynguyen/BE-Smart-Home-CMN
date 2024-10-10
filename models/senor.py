from pydantic import BaseModel
from datetime import datetime
now = datetime.now()

class SensorModel(BaseModel):
    name: str
    description: str
    temp: int
    humidity: int
    updated_time: str

