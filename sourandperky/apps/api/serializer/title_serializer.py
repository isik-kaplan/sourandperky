from rest_framework import serializers

from apps.sour_and_perky.models import Title
from .conditional_serializer import ConditionalSerializerMixin
from .title_channel_serializer import TitleChannelSerializer
from .user_serializer import UserSerializer


class TitleSerializer(ConditionalSerializerMixin, serializers.ModelSerializer):
    creator = UserSerializer()

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
        ]

        relational_fields = {
            'channels': lambda: TitleChannelSerializer(many=True)
        }
