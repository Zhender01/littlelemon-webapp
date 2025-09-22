from django.test import TestCase

# Create your tests here.
# restaurant/tests.py
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

class APISmokeTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="me", password="Pass12345")
    def auth(self):
        r = self.client.post("/api/auth/jwt/create/", {"username":"me","password":"Pass12345"}, format="json")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {r.data['access']}")
    def test_flow(self):
        self.auth()
        r1 = self.client.post("/api/menu-items/", {"title":"Pasta","price":"12.50","inventory":5}, format="json")
        self.assertEqual(r1.status_code, 201)
        r2 = self.client.post("/api/bookings/", {"name":"John","no_of_guests":2,"booking_date":"2025-10-01","booking_time":"18:30:00"}, format="json")
        self.assertEqual(r2.status_code, 201)
        r3 = self.client.get("/api/bookings/"); self.assertEqual(r3.status_code, 200); self.assertEqual(len(r3.data), 1)

