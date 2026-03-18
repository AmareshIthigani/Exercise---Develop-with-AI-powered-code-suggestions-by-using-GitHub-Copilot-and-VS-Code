def test_root_redirect(client):
    # Arrange
    # (client fixture provides the TestClient)
    
    # Act
    response = client.get("/", follow_redirects=False)
    
    # Assert
    assert response.status_code == 307  # Temporary redirect
    assert response.headers["location"] == "/static/index.html"


def test_get_activities_returns_all(client):
    # Arrange
    # (client fixture provides the TestClient)
    
    # Act
    response = client.get("/activities")
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert len(data) == 9  # Based on the 9 activities in app.py
    assert "Chess Club" in data
    assert "participants" in data["Chess Club"]