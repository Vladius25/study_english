from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from levels.models import Level


class TestLevels(APITestCase):
    @classmethod
    def setUpClass(cls):
        super(TestLevels, cls).setUpClass()
        cls.client = APIClient()
        cls.level = {
            "name": "Advanced",
            "code": "C1"
        }
        Level.objects.create(**cls.level)
        Level.objects.create(**cls.level)

    def test_return_200(self):
        response = self.client.get("/api/v1/levels/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_count_levels(self):
        response = self.client.get("/api/v1/levels/", format="json")
        self.assertEqual(len(response.data), 2)

    def test_get_level(self):
        response = self.client.get("/api/v1/levels/", format="json")
        self.level["id"] = 1
        self.assertDictEqual(response.data[0], self.level)
