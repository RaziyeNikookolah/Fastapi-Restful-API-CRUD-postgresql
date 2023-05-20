from fastapi import FastAPI
from config import engin
import model
import router

app = FastAPI()

app.include_router(router.router, prefix="/book", tags=["book"])


@app.get("/")
async def home():
    return "Welcome Home"


model.Base.metadata.create_all(bind=engin)
