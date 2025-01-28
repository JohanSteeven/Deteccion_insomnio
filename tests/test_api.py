import sys
import os

# Agregar la raíz del proyecto al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import create_app
import pytest

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200

def test_detect_no_image(client):
    response = client.post("/detect")
    assert response.status_code == 400
    assert b"No se proporcion\\u00f3 ninguna imagen" in response.data

