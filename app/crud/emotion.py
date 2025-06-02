# app/crud/emotion.py
from app.core.db import db
from app.models.emotion import EmotionCreate

async def insert_emotion(data: EmotionCreate):
    collection = db["emotions"]
    result = await collection.insert_one(data.dict())
    return {"inserted_id": str(result.inserted_id)}
