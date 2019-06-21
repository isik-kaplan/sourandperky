from rest_framework import serializers

from apps.sour_and_perky.models import Title
from .conditional_serializer import ConditionalSerializerMixin
from .title_channel import TitleChannelSerializer
from .user import UserSerializer


class TitleSerializer(ConditionalSerializerMixin, serializers.ModelSerializer):
    following = serializers.SerializerMethodField()

    @staticmethod
    def get_following(obj):
        return bool(getattr(obj, 'following', False))

    class Meta:
        model = Title
        fields = [
            'timestamp',
            'id',
            'text',
            'channels',
            'creator',
            'following',
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
