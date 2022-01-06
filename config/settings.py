"""Application settings"""
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://localhost/db")
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
DEBUG = os.getenv("DEBUG", "True") == "True"
