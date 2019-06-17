from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UAdmin
from django.db import models
from django.forms import TextInput
from django.utils.translation import gettext_lazy as _
from simple_history.admin import SimpleHistoryAdmin

from apps.notification.models import Notification
from ..models import User


class NotificationInline(admin.TabularInline):
    model = Notification
    max_num = 1
    formfield_overrides = {models.TextField: {'widget': TextInput(attrs={'size': '40'})}, }


@admin.register(User)
class UserAdmin(UAdmin, SimpleHistoryAdmin):
    inlines = [NotificationInline]
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Sour&Perky'), {
            'fields': ('bio', 'trophies')
        })
    )
    filter_horizontal = (
        'groups', 'user_permissions',
        'favs', 'likes', 'dislikes',
        'trophies', 'reported',
        'followed_titles', 'followed_users'
    )
