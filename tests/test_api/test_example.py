"""Module with tests."""
from __future__ import annotations

import requests


def test_example(get_test_data):
    """Test name."""
    response = requests.get('http://localhost:5050/foo/bar')
    print(response.text)
    assert response.status_code == 200


def test_example2():
    """Test name."""
    response = requests.get('http://localhost:5050/foo/bar/baz')
    print(response.text)
    assert response.status_code == 200
