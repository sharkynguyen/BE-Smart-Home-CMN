from pydantic import BaseModel

class MotorModel(BaseModel):
    name: str
    description: str
    status: int
    updated_time: str

