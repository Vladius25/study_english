from rest_framework import generics, permissions

from themes.models import Theme
from themes.serializers import ThemeSerializer, ThemeSerializerWithWords


class GetThemeView(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializerWithWords

