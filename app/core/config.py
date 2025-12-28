from pydantic_settings import BaseSettings
from zoneinfo import ZoneInfo

class Settings(BaseSettings):
    MONGO_URI: str
    MONGO_DB: str

    TIMEZONE: str = "UTC"

    @property
    def tz(self):
        return ZoneInfo(self.TIMEZONE)

    class Config:
        env_file = ".env"


settings = Settings()