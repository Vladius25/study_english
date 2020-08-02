from django.conf import settings
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class TestLevels(APITestCase):
    def test_without_secret(self):
        client = APIClient()
        response = client.get("/api/v1/levels/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_with_wrong_secret(self):
        client = APIClient()
        client.credentials(HTTP_SECRET="test")
        response = client.get("/api/v1/levels/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_with_correct_secret(self):
        client = APIClient()
        client.credentials(HTTP_SECRET=settings.API_SECRET)
        response = client.get("/api/v1/levels/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
