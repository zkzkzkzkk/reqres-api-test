import requests

def test_successful_login():
    url = "https://reqres.in/api/login"
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    res = requests.post(url, json=payload)
    assert res.status_code == 200
    assert "token" in res.json()

def test_login_missing_password():
    url = "https://reqres.in/api/login"
    payload = {
        "email": "peter@klaven"
    }
    res = requests.post(url, json=payload)
    assert res.status_code == 400
    assert res.json()["error"] == "Missing password"
