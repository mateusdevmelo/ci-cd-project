import os

def test_index_file_exists():
    file_path = os.path.join(os.path.dirname(__file__), "index.html")
    assert os.path.exists(file_path), "index.html does not exist"

def test_dockerfile_exists():
    file_path = os.path.join(os.path.dirname(__file__), "..", "Dockerfile")
    assert os.path.exists(file_path), "Dockerfile does not exist"

def test_gitignore_exists():
    file_path = os.path.join(os.path.dirname(__file__), "..", ".gitignore")
    assert os.path.exists(file_path), ".gitignore does not exist"
