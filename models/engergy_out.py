
from pydantic import BaseModel
from typing import Optional

class EnergyOutModel(BaseModel):
    vIn: float
    vOut: float
    cIn: float
    cOut: float
    pIn: float
    pOut: float
    temperature: float
    batPercent: float
    whP: float
    updated_time: str

