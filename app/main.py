from fastapi import FastAPI
from app.api import speech

app = FastAPI()

app.include_router(speech.router)
