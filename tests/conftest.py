"""
Pytest configuration and shared fixtures.
"""

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    """Test client for making API requests."""
    return TestClient(app)


@pytest.fixture
def mock_reasons():
    """Sample reasons data for testing."""
    return [
        {"message": "Test page not found", "reason": "This is a test reason", "category": "test"},
        {
            "message": "Another test 404",
            "reason": "Because testing is important",
            "category": "test",
        },
    ]
