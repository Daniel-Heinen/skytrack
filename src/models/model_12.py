"""Data model 12 for geolocation"""
from pydantic import BaseModel, Field, validator
from typing import Optional, List
from datetime import datetime

class GeoModel12(BaseModel):
    id: int
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)
    accuracy: float
    timestamp: datetime
    metadata: Optional[dict] = None
    tags: List[str] = []
    
    @validator("accuracy")
    def validate_accuracy(cls, v):
        if not 0 <= v <= 1:
            raise ValueError("Accuracy must be between 0 and 1")
        return v
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
