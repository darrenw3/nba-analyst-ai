from sqlalchemy import Column, Integer, String, Date
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
