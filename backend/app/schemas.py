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

class SeasonStatsResponse(BaseModel):
    id: int
    player_id: int
    season: str
    games_played: Optional[int] = None
    minutes_per_game: Optional[float] = None
    points_per_game: Optional[float] = None
    rebounds_per_game: Optional[float] = None
    assists_per_game: Optional[float] = None
    steals_per_game: Optional[float] = None
    blocks_per_game: Optional[float] = None
    field_goal_percentage: Optional[float] = None
    three_point_percentage: Optional[float] = None
    free_throw_percentage: Optional[float] = None

    class Config:
        from_attributes = True