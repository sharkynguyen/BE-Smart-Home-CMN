from pydantic import BaseModel

class PersonalInfo(BaseModel):
    age: str
    gender: str
    heartDesease: str
    otherDease: str
    heart: float
    oxygen: float

