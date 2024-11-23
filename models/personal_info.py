from pydantic import BaseModel

class PersonalInfo(BaseModel):
    age: str
    gender: str
    weight: float
    height: float
    heartDesease: str
    otherDease: str
    heart: float
    oxygen: float
    isPlayingSports: bool
    sport: str = None
