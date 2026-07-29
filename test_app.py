import unittest

from app import app
from main import create_greeting


class GreetingTest(unittest.TestCase):
    def setUp(self):
        app.config.update(TESTING=True)
        self.client = app.test_client()

    def test_create_greeting(self):
        self.assertEqual(create_greeting(" Ada ", " Lovelace "), "Hallo, Ada Lovelace!")

    def test_home_page_is_available(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn("Eine Begrüßung geht online.".encode(), response.data)

    def test_form_returns_greeting(self):
        response = self.client.post(
            "/",
            data={"first_name": "Ada", "last_name": "Lovelace"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("Hallo, Ada Lovelace!".encode(), response.data)
        self.assertIn(b"200 OK", response.data)

    def test_form_requires_both_names(self):
        response = self.client.post(
            "/",
            data={"first_name": "", "last_name": ""},
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("Bitte gib einen Vornamen ein.".encode(), response.data)
        self.assertIn("Bitte gib einen Nachnamen ein.".encode(), response.data)

    def test_health_check(self):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "ok"})


if __name__ == "__main__":
    unittest.main()
