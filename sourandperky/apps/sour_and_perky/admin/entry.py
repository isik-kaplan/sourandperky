from django.contrib import admin

from .common import CommonAdmin
from ..models import Entry


@admin.register(Entry)
class EntryAdmin(CommonAdmin):
    autocomplete_fields = ['title']
    list_display = ['id', 'author', 'title', 'readability', 'date']
    list_filter = ['title__text', 'author', 'readability', 'date']
    search_fields = ['text']
