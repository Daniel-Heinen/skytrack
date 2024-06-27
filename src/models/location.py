"""Data models for location"""
from pydantic import BaseModel

class Location(BaseModel):
    latitude: float
    longitude: float
    confidence: float
# Modified 2024-07-22
# Modified 2024-05-13
# Modified 2024-06-27
