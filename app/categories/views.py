from rest_framework import generics, permissions

from categories.models import Category
from categories.serializers import CategorySerializer


class GetCategoriesView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
