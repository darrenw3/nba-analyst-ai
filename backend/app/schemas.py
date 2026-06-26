from pydantic import BaseModel
from typing import Optional
from datetime import date

class PlayerCreate(BaseModel):
    name: str
    birthdate: Optional[date] = None
    team: Optional[str] = None
    position: Optional[str] = None
    height_inches: Optional[int] = None
    weight_lbs: Optional[int] = None

class PlayerResponse(BaseModel):    
    id: int
    name: str
    birthdate: Optional[date] = None
    team: Optional[str] = None
    position: Optional[str] = None
    height_inches: Optional[int] = None
    weight_lbs: Optional[int] = None

    class Config:
        from_attributes = True
