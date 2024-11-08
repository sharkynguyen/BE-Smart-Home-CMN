from pydantic import BaseModel
from datetime import datetime
now = datetime.now()

class SensorModel(BaseModel):
    name: str
    description: str
    temp: float
    humidity: float
    updated_time: str

