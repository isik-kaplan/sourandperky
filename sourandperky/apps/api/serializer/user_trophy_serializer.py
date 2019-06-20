from rest_framework import serializers

from apps.sour_and_perky.models import UserTrophy


class UserTrophySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTrophy
        fields = [
            'timestamp',
            'id',
            'name',
            'short_description',
            'description',
        ]
