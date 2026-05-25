from pydantic import field_validator
from pydantic_settings import BaseSettings


SUPPORTED_MODELS = [
    "text-embedding-3-small",
    "text-embedding-3-large",
    "text-embedding-ada-002",
]


class Settings(BaseSettings):
    OPENROUTER_API_KEY: str
    OPENROUTER_BASE_URL: str = "https://openrouter.ai/api/v1"
    OPENROUTER_MODEL: str = "text-embedding-3-small"

    @field_validator("OPENROUTER_MODEL")
    @classmethod
    def validate_model(cls, v):
        if v not in SUPPORTED_MODELS:
            raise ValueError(f"Unsupported model: {v}")
        return v

    class Config:
        env_file = ".env"


settings = Settings()