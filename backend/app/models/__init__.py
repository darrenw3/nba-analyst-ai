from sqlalchemy import Column, Integer, String
from app.database import Base

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    team = Column(String)
    position = Column(String)
    age = Column(Integer)
    height_inches = Column(Integer)
    weight_lbs = Column(Integer)
