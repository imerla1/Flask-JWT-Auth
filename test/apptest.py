import unittest
import requests

url = "http://127.0.0.1:5000/login"
data = {
    "username": "george",
    "password": "1234"
}

headers = {
    "Content-Type": "application/json"

}

class TestLoginResource(unittest.TestCase):
    
    def test_status_ok(self):
        resp = requests.post(
            url, json=data, headers=headers
        )
        self.assertEqual(resp.status_code, 200)

    
