from fastapi import FastAPI
from config import engin
import model

app = FastAPI()


@app.get("/")
async def home():
    return "Welcome Home"


model.Base.metadata.create_all(bind=engin)
