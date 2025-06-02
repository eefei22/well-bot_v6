# app/main.py
from fastapi import FastAPI
from app.api import api_router
from app.core.config import settings
from app.core.db import connect_to_mongo

app = FastAPI(title="Well-Bot API")

@app.on_event("startup")
async def startup_db():
    await connect_to_mongo()

app.include_router(api_router)
