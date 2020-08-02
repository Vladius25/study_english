from rest_framework import generics

from words.models import Word
from words.serializers import WordSerializer


class GetWordView(generics.RetrieveAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

