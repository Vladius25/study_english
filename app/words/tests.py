from django.conf import settings
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from words.models import Word
from words.serializers import WordSerializerShort


class TestWords(APITestCase):
    @classmethod
    def setUpClass(cls):
        super(TestWords, cls).setUpClass()
        cls.word = {
            "name": "to ask out",
            "translation": "Пригласить на свидание",
            "transcription": "tuː ɑːsk aʊt",
            "example": "John has asked Mary out several times.",
            "sound": "uploads/toaskout.mp3",
        }
        cls.word1 = Word.objects.create(**cls.word)
        cls.word2 = Word.objects.create(**cls.word)

    def setUp(self):
        self.client = APIClient()
        self.client.credentials(HTTP_SECRET=settings.API_SECRET)

    def test_return_200(self):
        response = self.client.get("/api/v1/words/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_word(self):
        response = self.client.get("/api/v1/words/1/", format="json")
        self.word["id"] = 1
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        del self.word["sound"]
        del response.data["sound"]
        self.assertDictEqual(response.data, self.word)

    def test_short_serialiser(self):
        serializer = WordSerializerShort()
        data = serializer.to_representation(self.word1)
        self.assertDictEqual(data, {"id": 1, "name": self.word["name"]})

    def test_sound_url_absolute(self):
        response = self.client.get("/api/v1/words/1/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["sound"].startswith("http"))
