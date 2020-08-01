from rest_framework import serializers

from categories.models import Category


class CategorySerializer(serializers.ModelSerializer):
    icon = serializers.SerializerMethodField()

    def get_icon(self, obj: Category):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.icon.url)

    class Meta:
        model = Category
        fields = "__all__"
