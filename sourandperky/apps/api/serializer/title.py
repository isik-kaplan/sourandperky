from rest_framework import serializers

from apps.sour_and_perky.models import Title
from .title_channel import TitleChannelSerializer
from .user import UserSerializer
from .conditional_serializer import ConditionalSerializerMixin


class TitleSerializer(ConditionalSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = [
            'timestamp',
            'id',
            'text',
            'channels',
            'creator',
        ]
        read_only_fields = [
            'creator',
        ]
        conditional_fields = [
            'channels',
            'creator',
        ]

        relational_fields = {
            'channels': lambda: TitleChannelSerializer(many=True, read_only=True),
            'creator': lambda: UserSerializer(read_only=True)
        }
