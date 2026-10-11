from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    APP_NAME: str = "Personal Hub API"
    APP_ENV: str = "development"
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    # API Key raw (dùng cho dev local) hoặc API_KEY_HASH (SHA-256 hash trên production)
    API_KEY: str = "phub_dev_key_123456"
    API_KEY_HASH: Optional[str] = None
    
    # Telegram Bot Secrets (Luôn load từ file .env hoặc env variables, không hardcode)
    TELEGRAM_BOT_TOKEN: str = ""
    TELEGRAM_CHAT_ID: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()
