from django.contrib import admin

from .common import CommonAdmin
from ..models import TitleChannel


@admin.register(TitleChannel)
class TitleChannelAdmin(CommonAdmin):
    ...
