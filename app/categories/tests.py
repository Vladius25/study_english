from time import sleep

from django.conf import settings
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from categories.models import Category


class TestCategories(APITestCase):
    @classmethod
    def setUpClass(cls):
        super(TestCategories, cls).setUpClass()
        cls.category = {
            "name": "1",
            "icon": "uploads/fun.png"
        }
        Category.objects.create(**cls.category)
        Category.objects.create(**cls.category)

    def setUp(self):
        self.client = APIClient()
        self.client.credentials(HTTP_SECRET=settings.API_SECRET)

    def test_return_200(self):
        response = self.client.get("/api/v1/categories/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_count_categories(self):
        response = self.client.get("/api/v1/categories/", format="json")
        self.assertEqual(len(response.data), 2)

    def test_icon_url_absolute(self):
        response = self.client.get("/api/v1/categories/", format="json")
        self.assertTrue(response.data[0]["icon"].startswith("http"))

    def test_get_category(self):
        response = self.client.get("/api/v1/categories/", format="json")
        self.category["id"] = 1
        del self.category["icon"]
        del response.data[0]["icon"]
        self.assertDictEqual(response.data[0], self.category)
