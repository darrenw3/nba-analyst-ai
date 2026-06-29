from fastapi import FastAPI
from app.database import engine
from app import models
from app.routers import players
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(players.router)
models.Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "The NBA Analyst AI is running!"}
