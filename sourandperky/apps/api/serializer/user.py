from contextlib import suppress

from rest_framework import serializers

from apps.sour_and_perky.models import User
from ..serializer.base_serializers import NotNullSerializerMixin


class UserSerializer(NotNullSerializerMixin, serializers.ModelSerializer):
    following = serializers.SerializerMethodField(allow_null=True)

    @staticmethod
    def get_following(obj):
        """
        In nested serializers it raises an attribute error,
        suppressing it means that we don't support nested annotation lookups
        """
        with suppress(AttributeError):
            return bool(obj.following)

    class Meta:
        model = User
        fields = [
            'timestamp',
            'id',
            'username',
            'first_name',
            'last_name',
            'avatar',
            'following',
        ]
