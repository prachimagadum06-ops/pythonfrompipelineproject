from app import app

def test_home_page():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Welcome to Flask running through Jenkins Pipeline" in response.data


def test_about_page():
    client = app.test_client()

    response = client.get("/about")

    assert response.status_code == 200
    assert b"About Page" in response.data