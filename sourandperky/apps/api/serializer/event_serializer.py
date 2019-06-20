from rest_framework import serializers

from apps.sour_and_perky.models import Event


class EventSerializer(serializers.ModelSerializer):
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
        ]
