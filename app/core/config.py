from pathlib import Path

from pydantic import BaseModel

from pydantic_settings import BaseSettings

DB_DIR = Path(__file__).parent.parent

DB_PATH = DB_DIR / "db.sqlite"


class DBSettings(BaseModel):
    url: str = f"sqlite+aiosqlite:///{DB_PATH}"
    echo: bool = True


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    db: DBSettings = DBSettings()


settings = Settings()
