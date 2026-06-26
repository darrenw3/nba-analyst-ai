from fastapi import APIRouter, Depends, HTTPException
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

@router.get("/players/{player_id}", response_model=PlayerResponse)
def get_player(player_id: int, db: Session = Depends(get_db)):
    player = db.query(models.Player).filter(models.Player.id == player_id).first()
    if player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return player

@router.get("/players/search/query", response_model=List[PlayerResponse])
def search_players(name: str, db: Session = Depends(get_db)):
    players = db.query(models.Player).filter(models.Player.name.ilike(f"%{name}%")).all()
    if not players:
        raise HTTPException(status_code=404, detail="No players found")
    return players
