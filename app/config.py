import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGO_URL: str = os.getenv("MONGO_URL", "mongodb://localhost:27017")
    MONGO_DB: str = os.getenv("MONGO_DB", "link_apex_db")

    class Config:
        env_file = ".env"

settings = Settings()
