import unittest
import requests

BASE_URL = "http://localhost:8080"

class TestFastAPI(unittest.TestCase):

    def test_root(self):
        r = requests.get(f"{BASE_URL}/")
        self.assertEqual(r.status_code, 200)
        self.assertIn("message", r.json())

    def test_hello_query(self):
        r = requests.get(f"{BASE_URL}/Hello", params={"name": "Alice", "age": 25})
        self.assertEqual(r.status_code, 200)

    def test_hello_path(self):
        r = requests.get(f"{BASE_URL}/hello/Alice/25")
        self.assertEqual(r.status_code, 200)

    def test_hello_post(self):
        payload = {"name": "Alice", "age": 25}
        r = requests.post(f"{BASE_URL}/hello_personclass", json=payload)
        self.assertEqual(r.status_code, 200)

    def test_time(self):
        r = requests.get(f"{BASE_URL}/time")
        self.assertIn("current_time", r.json())

    def test_greet(self):
        r = requests.get(f"{BASE_URL}/greet", params={"name": "Alice", "city": "NYC"})
        self.assertEqual(r.status_code, 200)

    def test_square(self):
        r = requests.get(f"{BASE_URL}/Square", params={"number": 4})
        self.assertEqual(r.json()["square"], 16)

    def test_reverse(self):
        r = requests.get(f"{BASE_URL}/reverse", params={"string": "hello"})
        self.assertEqual(r.json()["reversed"], "olleh")

    def test_status(self):
        r = requests.get(f"{BASE_URL}/status", params={"is_online": "true"})
        self.assertEqual(r.json()["status"], "Online")

    def test_user(self):
        r = requests.get(f"{BASE_URL}/user/1")
        self.assertIn("name", r.json())

    def test_header_info(self):
        r = requests.get(f"{BASE_URL}/header-info", headers={"User-Agent": "TestAgent"})
        self.assertEqual(r.json()["User-Agent"], "TestAgent")

    def test_cookie_info(self):
        r = requests.get(f"{BASE_URL}/cookie-info", cookies={"session_id": "abc123"})
        self.assertEqual(r.json()["Session-ID"], "abc123")

if __name__ == "__main__":
    unittest.main()
