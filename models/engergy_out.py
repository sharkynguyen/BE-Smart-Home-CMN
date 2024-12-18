
from pydantic import BaseModel
from typing import Optional

class EnergyOutModel(BaseModel):
    vIn: float
    vOut: float
    cIn: float
    cOut: float
    pIn: float
    pOut: float
    tempearturePl1: float
    batPercent: float
    whp: float
    updated_time: str

