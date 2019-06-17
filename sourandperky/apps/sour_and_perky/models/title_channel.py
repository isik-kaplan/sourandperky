from django.db import models

from .common import CommonFields


class TitleChannel(CommonFields):
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    is_main = models.BooleanField(default=True)

    def __str__(self):
        return self.name