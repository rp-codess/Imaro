from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    APP_NAME: str = "Imaro Phase 1 API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Database
    DATABASE_URL: str
    
    # Firebase
    FIREBASE_CREDENTIALS_PATH: str
    FIREBASE_PROJECT_ID: str
    
    # JWT
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440
    REFRESH_TOKEN_EXPIRE_DAYS: int = 30
    
    # Environment
    DEBUG: bool = True
    ENVIRONMENT: str = "development"
    
    # CORS
    ALLOWED_HOSTS: list = ["*"]
    
    class Config:
        env_file = ".env"

settings = Settings()
