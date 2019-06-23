from django.conf import settings
from django.db import models

from .common import CommonFields, first_user_id


class Entry(CommonFields):
    title = models.ForeignKey('Title', on_delete=models.CASCADE, related_name='entries')
    text = models.TextField(max_length=2500, null=True, blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        default=first_user_id,
        on_delete=models.SET_DEFAULT,
        related_name='entries'
    )
    readability = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = 'Entries'
