"""Core functionality tests"""
import pytest

def test_basic():
    assert True

def test_location_validation():
    from src.utils.helpers import validate_coordinates
    assert validate_coordinates(0, 0) == True
