from django.contrib import admin

from .common import CommonAdmin
from ..models import Event


@admin.register(Event)
class EventAdmin(CommonAdmin):
    ...
