from pydantic import BaseSettings


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./test.db"

settings = Settings()