from django.db import models

from .common import CommonFields


class UserTrophy(CommonFields):
    name = models.CharField(max_length=100, null=True, blank=True)
    short_description = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'User Trophies'
