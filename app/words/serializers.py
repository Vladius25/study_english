from rest_framework import serializers

from words.models import Word


class WordSerializer(serializers.ModelSerializer):
    sound = serializers.SerializerMethodField()

    def get_sound(self, obj: Word):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.sound.url)

    class Meta:
        model = Word
        fields = "__all__"
