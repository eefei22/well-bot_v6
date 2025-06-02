# app/models/emotion.py
from pydantic import BaseModel

class EmotionCreate(BaseModel):
    user_id: str
    heart_rate: float
    emotion: str
