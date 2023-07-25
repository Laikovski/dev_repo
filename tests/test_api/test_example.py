import requests


def test_example():
    response = requests.get('http://localhost:5050/foo/bar')
    print(response.text)
    assert response.status_code == 200


def test_example2():
    response = requests.get('http://localhost:5050/foo/bar/baz')
    print(response.text)
    assert response.status_code == 200
