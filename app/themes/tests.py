from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from categories.models import Category
from levels.models import Level
from themes.models import Theme


class TestThemes(APITestCase):
    @classmethod
    def setUpClass(cls):
        super(TestThemes, cls).setUpClass()
        cls.client = APIClient()
        cls.themes, categories, levels = [], [], []
        for _ in range(3):
            categories.append(Category.objects.create(name="test", icon="uploads/icon.png"))
        for _ in range(3):
            levels.append(Level.objects.create(name="test", code="0"))
        for i in range(len(categories)):
            for k in range(len(levels)):
                cls.themes.append(
                    Theme.objects.create(category=categories[i],
                                         level=levels[k],
                                         name="test", photo="uploads/photo.png")
                )

    def test_return_200(self):
        response = self.client.get("/api/v1/themes/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_count_themes(self):
        response = self.client.get("/api/v1/themes/", format="json")
        self.assertEqual(len(response.data), 9)

    def test_filter_themes(self):
        response = self.client.get(f"/api/v1/themes/?category=1", format="json")
        self.assertEqual(len(response.data), 3)

    def test_filter_themes_two_param(self):
        response = self.client.get(f"/api/v1/themes/?category=1&level=2", format="json")
        self.assertEqual(len(response.data), 1)

    def test_filter_theme_has_no_words(self):
        response = self.client.get(f"/api/v1/themes/", format="json")
        self.assertFalse("words" in response.data)

    def test_get_theme_has_words(self):
        response = self.client.get(f"/api/v1/themes/1/", format="json")
        self.assertTrue("words" in response.data)

    def test_get_theme(self):
        response = self.client.get(f"/api/v1/themes/1/", format="json")
        del response.data["photo"]
        self.assertDictEqual(response.data, {"id": 1, "name": "test", "category": 1, "level": 1, "words": []})

    def test_photo_url_absolute(self):
        response = self.client.get("/api/v1/themes/1/", format="json")
        self.assertTrue(response.data["photo"].startswith("http"))








