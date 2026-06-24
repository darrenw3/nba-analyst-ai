from sqlalchemy import Column, Integer, String
from app.database import Base

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    team = Column(String)
    position = Column(String)
    height_inches = Column(Integer)
    weight_lbs = Column(Integer)
