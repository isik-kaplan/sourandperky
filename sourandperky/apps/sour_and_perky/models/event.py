from datetime import datetime

from django.db import models

from .common import CommonFields


class Event(CommonFields):
    name = models.CharField(max_length=50, null=True, blank=True)
    short_desc = models.CharField(max_length=250, null=True, blank=True)
    desc = models.TextField(max_length=2500, null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def active(self):
        return self.start_date < datetime.now() < self.end_date
