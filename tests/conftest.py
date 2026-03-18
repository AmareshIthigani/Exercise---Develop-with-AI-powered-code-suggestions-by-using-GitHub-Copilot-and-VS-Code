import pytest
from fastapi.testclient import TestClient
from src.app import app, activities

# Store original activities data
original_activities = {}
for key, value in activities.items():
    original_activities[key] = value.copy()
    original_activities[key]["participants"] = value["participants"].copy()

@pytest.fixture
def client():
    """Fixture to provide a TestClient for the FastAPI app."""
    return TestClient(app)

@pytest.fixture(autouse=True)
def reset_activities():
    """Reset activities data before each test to ensure isolation."""
    activities.clear()
    for key, value in original_activities.items():
        activities[key] = value.copy()
        activities[key]["participants"] = value["participants"].copy()