from rest_framework import generics, permissions

from words.models import Word
from words.serializers import WordSerializer


class GetWordView(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Word.objects.all()
    serializer_class = WordSerializer

