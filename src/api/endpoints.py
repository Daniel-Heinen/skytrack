"""API endpoints"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "healthy"}
# Modified 2025-09-23
