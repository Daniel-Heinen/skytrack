"""Comprehensive tests for processor module 66"""
import pytest
import numpy as np
import torch
from src.processor_66 import AdvancedGeoProcessor66, GeoLocation

class TestGeoProcessor66:
    
    @pytest.fixture
    def processor(self):
        return AdvancedGeoProcessor66()
    
    def test_initialization(self, processor):
        assert processor.input_dim == 512
        assert processor.hidden_dim == 256
        assert isinstance(processor, torch.nn.Module)
    
    def test_forward_pass(self, processor):
        x = torch.randn(1, 512)
        output = processor.forward(x)
        assert output.shape == (1, 2)
    
    @pytest.mark.asyncio
    async def test_predict_location(self, processor):
        features = np.random.randn(512)
        location = await processor.predict_location(features)
        assert isinstance(location, GeoLocation)
        assert -90 <= location.latitude <= 90
        assert -180 <= location.longitude <= 180
        assert 0 <= location.confidence <= 1
    
    def test_model_parameters(self, processor):
        params = list(processor.parameters())
        assert len(params) > 0
    
    def test_training_mode(self, processor):
        processor.train()
        assert processor.training == True
        processor.eval()
        assert processor.training == False
