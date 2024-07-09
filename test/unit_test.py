import pytest
import requests
import os
import csv

# Assuming your FastAPI app is running on localhost:8000
BASE_URL = "http://localhost:8000"

@pytest.fixture(scope="module")
def setup_teardown():
    # Start the FastAPI app here if needed
    yield
    # Clean up after tests if needed
    if os.path.exists('text_image_mapping.csv'):
        os.remove('text_image_mapping.csv')

def test_insert_text_on_image(setup_teardown):
    url = f"{BASE_URL}/insert_text_on_image/"
    with open("test_image.jpg", "rb") as image_file:
        files = {"image": ("test_image.jpg", image_file, "image/jpeg")}
        data = {
            "text": "Hello World",
            "text_color": "red",
            "font_size_ratio": 0.1,
            "font_path": "arial.ttf"  # Ensure this font exists in your test environment
        }
        response = requests.post(url, files=files, data=data)
    
    assert response.status_code == 200
    assert "base64_image" in response.json()
    assert "static_url" in response.json()

def test_get_texts(setup_teardown):
    url = f"{BASE_URL}/texts/"
    response = requests.get(url)
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_text_exists(setup_teardown):
    url = f"{BASE_URL}/text_exists/"
    params = {"text": "Hello World"}
    response = requests.get(url, params=params)
    
    assert response.status_code == 200
    assert "exists" in response.json()
    assert "text" in response.json()

def test_csv_file_creation(setup_teardown):
    assert os.path.exists('text_image_mapping.csv')
    with open('text_image_mapping.csv', mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        assert len(rows) > 0
        assert rows[0][0] == "Hello World"

if __name__ == "__main__":
    pytest.main()