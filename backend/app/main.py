from fastapi import FastAPI
from app.database import engine
from app import models
from app.routers import players

app = FastAPI()
app.include_router(players.router)
models.Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "The NBA Analyst AI is running!"}
