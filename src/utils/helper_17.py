"""Utility helper module 17"""
import numpy as np
from typing import List, Dict, Any
import json
import hashlib

class GeoHelper17:
    """Helper utilities for geolocation processing"""
    
    @staticmethod
    def validate_coordinates(lat: float, lng: float) -> bool:
        """Validate geographic coordinates"""
        return -90 <= lat <= 90 and -180 <= lng <= 180
    
    @staticmethod
    def calculate_distance(coord1: tuple, coord2: tuple) -> float:
        """Calculate distance between two coordinates"""
        lat1, lng1 = coord1
        lat2, lng2 = coord2
        return np.sqrt((lat2 - lat1)**2 + (lng2 - lng1)**2)
    
    @staticmethod
    def normalize_data(data: np.ndarray) -> np.ndarray:
        """Normalize input data"""
        return (data - np.mean(data)) / np.std(data)
    
    @staticmethod
    def hash_location(lat: float, lng: float) -> str:
        """Generate hash for location"""
        location_str = f"{lat},{lng}"
        return hashlib.sha256(location_str.encode()).hexdigest()
    
    @staticmethod
    def parse_exif(data: Dict[str, Any]) -> Dict:
        """Parse EXIF data for geolocation"""
        return {
            "lat": data.get("GPSLatitude"),
            "lng": data.get("GPSLongitude"),
            "altitude": data.get("GPSAltitude")
        }
