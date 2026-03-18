def test_signup_success(client):
    # Arrange
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"
    
    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert email in data["message"]


def test_signup_nonexistent_activity(client):
    # Arrange
    activity_name = "Nonexistent Activity"
    email = "student@mergington.edu"
    
    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    
    # Assert
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert "Activity not found" in data["detail"]


def test_signup_duplicate_email(client):
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"  # Already in participants
    
    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    
    # Assert
    assert response.status_code == 400
    data = response.json()
    assert "detail" in data
    assert "already signed up" in data["detail"]


def test_signup_activity_full(client):
    # Arrange
    activity_name = "Tennis Club"  # Max 10 participants, has 2
    emails = ["student1@mergington.edu", "student2@mergington.edu", "student3@mergington.edu",
              "student4@mergington.edu", "student5@mergington.edu", "student6@mergington.edu",
              "student7@mergington.edu", "student8@mergington.edu"]  # Fill to max
    
    # Fill the activity first
    for email in emails:
        client.post(f"/activities/{activity_name}/signup?email={email}")
    
    # Act - try to add one more
    response = client.post(f"/activities/{activity_name}/signup?email=overflow@mergington.edu")
    
    # Assert
    assert response.status_code == 400
    data = response.json()
    assert "detail" in data
    assert "full" in data["detail"]