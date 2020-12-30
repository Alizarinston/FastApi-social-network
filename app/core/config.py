import secrets
from os import environ

from pydantic import BaseSettings

DB_USER = environ.get("DB_USER", "user")
DB_PASS = environ.get("DB_PASSWORD", "password")
DB_NAME = environ.get("DB_NAME", "social-network")
DB_HOST = environ.get("DB_HOST", "localhost")


class Settings(BaseSettings):
    # SECRET_KEY: str = "ebHS3-oNtLcoUNDkAJImkdaT4tq8T6DrV9_Vf3zudGc"
    SECRET_KEY: str = secrets.token_urlsafe(32)

    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    RESPONSE_MODELS_LIMIT: int = 100

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
    )

    class Config:
        case_sensitive = True


settings = Settings()
