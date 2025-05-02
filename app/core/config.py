from pathlib import Path

from pydantic import BaseModel

from pydantic_settings import BaseSettings

DB_DIR = Path(__file__).parent.parent

DB_PATH = DB_DIR / "db.sqlite"
DB_NAME = "status_dashboard_test"
DB_USER = "sdb"
DB_PASSWORD = "sdb"
DB_HOST = "localhost"
DB_PORT = "25433"


class DBSettings(BaseModel):
    url: str = (
        f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    echo: bool = True


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    db: DBSettings = DBSettings()


settings = Settings()
