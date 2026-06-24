from pydantic import BaseModel
from typing import Optional

class PlayerCreate(BaseModel):
    name: str
    age: Optional[int] = None
    team: Optional[str] = None
    position: Optional[str] = None
    height_inches: Optional[int] = None
    weight_lbs: Optional[int] = None

class PlayerResponse(BaseModel):    
    id: int
    name: str
    age: Optional[int] = None
    team: Optional[str] = None
    position: Optional[str] = None
    height_inches: Optional[int] = None
    weight_lbs: Optional[int] = None

    class Config:
        from_attributes = True
