from django.contrib import admin

from .common import CommonAdmin
from ..models import Title


@admin.register(Title)
class TitleAdmin(CommonAdmin):
    filter_horizontal = ['channels']
    search_fields = ['text']
