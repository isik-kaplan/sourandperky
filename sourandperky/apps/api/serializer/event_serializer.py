from rest_framework import serializers

from apps.sour_and_perky.models import Event


class EventSerializer(serializers.ModelSerializer):
    is_active = serializers.SerializerMethodField()

    @staticmethod
    def get_is_active(obj):
        return obj.is_active

    class Meta:
        model = Event
        fields = [
            'timestamp',
            'id',
            'name',
            'short_desc',
            'desc',
            'start_date',
            'end_date',
            'is_active',
        ]
