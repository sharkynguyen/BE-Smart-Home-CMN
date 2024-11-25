
from pydantic import BaseModel
from typing import Optional

class EnergyOutModel(BaseModel):
    vIn: float
    vOut: float
    iIn: float
    iOut: float
    pOut: float
    pIn: float
    temperature: float
    updated_time: str

