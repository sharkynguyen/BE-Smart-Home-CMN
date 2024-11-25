from pydantic import BaseModel
from typing import Optional

class EnergyInModel(BaseModel):
    vMin: float
    vMax: float
    l: float
    temperatureFan: float
    temperatureMax: float
    updated_time: str
