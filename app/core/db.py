# app/core/db.py
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

db = None

async def connect_to_mongo():
    global db
    client = AsyncIOMotorClient(settings.MONGODB_URL)
    db = client["wellbot"]
