from django.contrib import admin

from .common import CommonAdmin
from ..models import Entry


@admin.register(Entry)
class EntryAdmin(CommonAdmin):
    autocomplete_fields = ['title']
    list_display = ['id', 'author', 'title', 'readability']
    list_filter = ['title__text', 'author', 'readability']
    search_fields = ['text']
