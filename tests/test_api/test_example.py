import requests



def test_example():
    response = requests.get('http://localhost:5050/foo/bar')
    assert response.status_code == 200
