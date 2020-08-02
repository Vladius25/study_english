from rest_framework import generics, permissions

from levels.models import Level
from levels.serializers import LevelSerializer


class GetLevelsView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

