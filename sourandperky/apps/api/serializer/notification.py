from rest_framework import serializers

from apps.notification.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            'timestamp',
            'id',
            'title',
            'short_desc',
            'desc',
            'is_read',
            'is_archived',
            'type',
        ]
