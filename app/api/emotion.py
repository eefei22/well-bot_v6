# app/api/emotion.py
from fastapi import APIRouter, HTTPException
from app.models.emotion import EmotionCreate
from app.crud.emotion import insert_emotion

router = APIRouter()

@router.post("/emotions")
async def create_emotion(payload: EmotionCreate):
    return await insert_emotion(payload)
