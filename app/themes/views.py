from rest_framework import generics, permissions

from themes.models import Theme
from themes.serializers import ThemeSerializer, ThemeSerializerWithWords


class GetThemeView(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializerWithWords


class GetThemesView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ThemeSerializer

    def get_queryset(self):
        queryset = Theme.objects.all()
        for param_name in ("category", "level"):
            param = self.request.query_params.get(param_name, None)
            if param:
                queryset = queryset.filter(**{param_name: param})
        return queryset
