from rest_framework import serializers

from apps.sour_and_perky.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'timestamp',
            'id',
            'username',
            'first_name',
            'last_name',
            'avatar',
        ]
