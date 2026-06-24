from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app.schemas import PlayerCreate, PlayerResponse
from typing import List

router = APIRouter()

@router.post("/players/", response_model=PlayerResponse)
def create_player(player: PlayerCreate, db: Session = Depends(get_db)):
    db_player = models.Player(**player.model_dump())
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player

@router.get("/players/", response_model=List[PlayerResponse])
def get_players(db: Session = Depends(get_db)):
    players = db.query(models.Player).all()
    return players
