from rest_framework import viewsets

from apps.notification.models import Notification
from ..filters import NotificationFilter
from ..serializer import NotificationSerializer


class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    filterset_class = NotificationFilter
    search_fields = ['desc', 'short_desc']
