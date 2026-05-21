from dotenv import load_dotenv
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    openrouter_api_key: str = Field(..., alias="OPENROUTER_API_KEY")
    openrouter_base_url: str = Field("https://openrouter.ai/api/v1", alias="OPENROUTER_BASE_URL")
    openrouter_model: str = Field("text-embedding-3-small", alias="OPENROUTER_MODEL")

    @field_validator("openrouter_model")
    @classmethod
    def validate_model(cls, v: str) -> str:
        allowed_models = {
            "text-embedding-3-small",
            "text-embedding-3-large",
            "text-embedding-ada-002",
        }
        if v not in allowed_models:
            raise ValueError(
                f"Invalid model: '{v}'. Must be one of: {sorted(allowed_models)}"
            )
        return v

# Instantiate settings immediately to trigger validation on startup
settings = Settings()