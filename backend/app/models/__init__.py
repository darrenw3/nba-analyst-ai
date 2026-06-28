from sqlalchemy import Column, Float, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    birthdate = Column(Date)
    team = Column(String)
    position = Column(String)
    height_inches = Column(Integer)
    weight_lbs = Column(Integer)

    season_stats = relationship("SeasonStats", back_populates="player", cascade="all, delete-orphan")

class SeasonStats(Base):
    __tablename__ = "season_stats"

    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey("players.id"), nullable=False)
    season = Column(String, nullable=False)
    games_played = Column(Integer)
    minutes_per_game = Column(Float)
    points_per_game = Column(Float)
    rebounds_per_game = Column(Float)
    assists_per_game = Column(Float)
    steals_per_game = Column(Float)
    blocks_per_game = Column(Float)
    field_goal_percentage = Column(Float)
    three_point_percentage = Column(Float)
    free_throw_percentage = Column(Float)


    player = relationship("Player", back_populates="season_stats")
