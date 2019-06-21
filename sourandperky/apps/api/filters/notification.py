from django_filters import rest_framework as filters

from apps.notification.models import Notification


class NotificationFilter(filters.FilterSet):
    class Meta:
        model = Notification
        fields = {
            'is_read': ['exact'],
            'is_archived': ['exact']
        }
