from rest_framework import serializers

from apps.sour_and_perky.models import User


class UserSerializer(serializers.ModelSerializer):
    following = serializers.SerializerMethodField()

    @staticmethod
    def get_following(obj):
        return bool(getattr(obj, 'following'))

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
