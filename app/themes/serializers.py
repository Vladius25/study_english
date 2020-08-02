from rest_framework import serializers

from themes.models import Theme
from words.serializers import WordSerializerShort


class ThemeSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    def get_photo(self, obj: Theme):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.photo.url)

    class Meta:
        model = Theme
        exclude = ("words",)


class ThemeSerializerWithWords(ThemeSerializer):
    words = WordSerializerShort(many=True, read_only=True)

    class Meta:
        model = Theme
        fields = "__all__"
