from fastapi import FastAPI
from app.api import speech
from dotenv import load_dotenv


load_dotenv()

# Then import app.api etc


app = FastAPI()

app.include_router(speech.router)
