from rest_framework import serializers

from apps.sour_and_perky.models import TitleChannel


class TitleChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TitleChannel
        fields = [
            'timestamp',
            'id',
            'name',
            'description',
            'is_main',
        ]
