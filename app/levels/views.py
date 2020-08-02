from rest_framework import generics

from levels.models import Level
from levels.serializers import LevelSerializer


class GetLevelsView(generics.ListAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

