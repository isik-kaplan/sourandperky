from django.conf import settings
from django.db import models

from .common import CommonFields, first_user_id


class Title(CommonFields):
    text = models.CharField(max_length=50, null=True, unique=True)
    channels = models.ManyToManyField('TitleChannel', related_name="titles")
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        default=first_user_id,
        on_delete=models.SET_DEFAULT
    )

    def __str__(self):
        return self.text

    @property
    def random_entry(self):
        return self.entries.filter(readability=True).random().get()

    @property
    def has_readable_entries(self):
        return self.entries.filter(readability=True).exists()
