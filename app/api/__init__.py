from fastapi import APIRouter
from app.api import emotion

api_router = APIRouter()
api_router.include_router(emotion.router, prefix="", tags=["Emotion"])
