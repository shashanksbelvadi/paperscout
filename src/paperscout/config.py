from functools import lru_cache
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "Paperscout"
    qdrant_host: str
    qdrant_api_key: SecretStr
    gemini_api_key: SecretStr

@lru_cache
def get_settings() -> Settings:
    return Settings()
