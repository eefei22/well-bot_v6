# app/core/config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    MONGODB_URL: str

    class Config:
        env_file = ".env"

settings = Settings()


#Load this with settings.MONGODB_URL anywhere in your code.