"""
Tests for API endpoints.
Because untested code is just a future bug 🐛
"""
import pytest
from fastapi.testclient import TestClient


def test_health_check(client: TestClient):
    """Health check should always return 200."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_home_endpoint(client: TestClient):
    """Root endpoint should return HTML homepage."""
    response = client.get("/")
    assert response.status_code == 200
    # Now returns HTML, not JSON
    assert "text/html" in response.headers["content-type"]
    assert "404-as-a-Service" in response.text


def test_get_404_endpoint(client: TestClient):
    """API 404 endpoint should return a reason."""
    response = client.get("/api/v1/404")
    assert response.status_code == 200
    data = response.json()
    
    # Check structure
    assert "status_code" in data
    assert "error" in data
    assert "message" in data
    assert "reason" in data
    
    # Validate values
    assert data["status_code"] == 404
    assert data["error"] == "Not Found"


def test_get_random_404_endpoint(client: TestClient):
    """Random 404 alias should work identically."""
    response = client.get("/api/v1/404/random")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "reason" in data


def test_list_all_reasons(client: TestClient):
    """Reasons endpoint should return all available reasons."""
    response = client.get("/api/v1/reasons")
    assert response.status_code == 200
    data = response.json()
    
    assert "total" in data
    assert "reasons" in data
    assert isinstance(data["reasons"], list)
    assert data["total"] == len(data["reasons"])
    
    # Each reason should have required fields
    if data["reasons"]:
        reason = data["reasons"][0]
        assert "message" in reason
        assert "reason" in reason


def test_undefined_route_returns_404(client: TestClient):
    """Any undefined route should return creative 404 (HTML by default)."""
    response = client.get("/this/does/not/exist")
    assert response.status_code == 404
    
    # Should return HTML for browser clients
    assert "text/html" in response.headers["content-type"]
    assert "404" in response.text


def test_undefined_route_json_with_header(client: TestClient):
    """Undefined route with JSON accept header should return JSON."""
    response = client.get(
        "/this/does/not/exist",
        headers={"Accept": "application/json"}
    )
    assert response.status_code == 404
    data = response.json()
    
    # Should have our custom 404 structure
    assert "error" in data
    assert "message" in data
    assert "reason" in data


def test_404_randomness(client: TestClient):
    """Multiple requests should eventually return different reasons."""
    responses = []
    for _ in range(10):
        response = client.get("/api/v1/404")
        responses.append(response.json()["message"])
    
    # With 20 reasons, 10 requests should give us some variety
    # (Though technically could all be the same due to randomness)
    unique_messages = len(set(responses))
    assert unique_messages > 1, "Should get different messages across requests"


def test_api_json_accept_header(client: TestClient):
    """Requests with JSON accept header should get JSON response."""
    response = client.get(
        "/undefined/path",
        headers={"Accept": "application/json"}
    )
    assert response.status_code == 404
    assert response.headers["content-type"] == "application/json"


def test_web_404_endpoint(client: TestClient):
    """Web 404 endpoint should return beautiful HTML."""
    response = client.get("/404")
    assert response.status_code == 404
    assert "text/html" in response.headers["content-type"]
    assert "404" in response.text
    assert "404-as-a-Service" in response.text


def test_web_404_with_category(client: TestClient):
    """Web 404 with category should return themed page."""
    response = client.get("/404?category=gaming")
    assert response.status_code == 404
    assert "text/html" in response.headers["content-type"]
    assert "gaming" in response.text.lower()


def test_web_404_invalid_category_fallback(client: TestClient):
    """Invalid category should fallback to random."""
    response = client.get("/404?category=invalid-category")
    assert response.status_code == 404
    assert "text/html" in response.headers["content-type"]
