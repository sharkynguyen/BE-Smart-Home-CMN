from pydantic import BaseModel
from typing import Optional

class DeviceModel(BaseModel):
    name: str
    description: str
    status: int
    updated_time: str

