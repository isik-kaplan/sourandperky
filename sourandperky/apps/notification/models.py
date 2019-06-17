import uuid

from django.conf import settings
from django.db import models
from django.utils import timezone

from utils.choices import Choices


class Notification(models.Model):
    # pk
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # timestamp
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    # user
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')

    # information
    title = models.CharField(max_length=50)
    short_desc = models.CharField(max_length=100)
    desc = models.TextField(max_length=1000)

    # status
    is_read = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)

    # type
    types = Choices({
        'NOTIFICATION': ...,
        'NOTIFICATION_AND_EMAIL': ...,
        'NOTIFICATION_EMAIL_AND_MESSAGE': ...,
    })

    type = models.CharField(choices=types.choices, max_length=50, default=types.NOTIFICATION)
