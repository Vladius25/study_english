import json

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from categories.models import Category


class TestCategories(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = {
            "name": "1",
            "icon": "https://icon/url"
        }

    def test_return_200(self):
        response = self.client.get("/api/v1/categories/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_count_categories(self):
        Category.objects.create(**self.category)
        Category.objects.create(**self.category)
        response = self.client.get("/api/v1/categories/", format="json")
        self.assertEqual(len(response.data), 2)
