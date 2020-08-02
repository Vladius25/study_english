from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from words.models import Word


class TestCategories(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.word = {
            "id": 1,
            "name": "to ask out",
            "translation": "Пригласить на свидание",
            "transcription": "tuː ɑːsk aʊt",
            "example": "John has asked Mary out several times.",
            "sound": "uploads/toaskout.mp3",
        }
        Word.objects.create(**self.word)

    def test_return_200(self):
        response = self.client.get("/api/v1/words/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_word(self):
        response = self.client.get("/api/v1/words/1/", format="json")
        del self.word["sound"]
        del response.data["sound"]
        self.assertDictEqual(response.data, self.word)

    def test_sound_url_absolute(self):
        response = self.client.get("/api/v1/words/1/", format="json")
        self.assertTrue(response.data["sound"].startswith("http"))
