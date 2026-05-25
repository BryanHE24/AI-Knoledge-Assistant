from pathlib import Path
from fastapi import APIRouter
from app.core.config import settings

router = APIRouter()


@router.get("/health")
def health():
    vectorstore_exists = Path("data/vectorstore").exists()

    return {
        "status": "ok" if vectorstore_exists else "degraded",
        "config": "loaded" if settings.OPENROUTER_API_KEY else "missing",
        "vectorstore": (
            "available"
            if vectorstore_exists
            else "missing"
        )
    }