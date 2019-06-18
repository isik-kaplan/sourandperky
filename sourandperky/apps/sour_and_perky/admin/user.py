from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UAdmin
from django.contrib.auth.forms import UserCreationForm as UCreateF, UserChangeForm as UChangeF
from django.db import models
from django.forms import TextInput
from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _
from simple_history.admin import SimpleHistoryAdmin
from django.contrib.admin.widgets import FilteredSelectMultiple

from apps.notification.models import Notification
from ..models import User


class NotificationInline(admin.TabularInline):
    model = Notification
    max_num = 1
    formfield_overrides = {models.TextField: {'widget': TextInput(attrs={'size': '40'})}, }


class UserCreationForm(UCreateF):
    class Meta(UCreateF.Meta):
        model = User


class UserChangeForm(UChangeF):
    class Meta(UChangeF.Meta):
        widgets = {
            'user_permissions': FilteredSelectMultiple(is_stacked=False, verbose_name=_('Permissions')),
            'groups': FilteredSelectMultiple(is_stacked=False, verbose_name=_('Groups')),
            'trophies': FilteredSelectMultiple(is_stacked=False, verbose_name=_('Trophies')),
        }
        model = User


@admin.register(User)
class UserAdmin(UAdmin, SimpleHistoryAdmin):
    add_form_template = 'admin/auth/user/add_form.html'
    add_fieldsets = UAdmin.add_fieldsets
    form = UserChangeForm
    add_form = UserCreationForm

    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            return self.add_form
        else:
            return self.form

    inlines = [NotificationInline]

    def get_fieldsets(self, request, obj=None):
        extra = ()
        if obj:
            return (
                (None, {'fields': extra + ('avatar_as_picture', 'avatar', 'username', 'password')}),
                (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
                (_('Permissions'), {
                    'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
                }),
                (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
                (_('Sour&Perky'), {
                    'fields': ('bio', 'trophies')
                })
            )
        else:
            return self.add_fieldsets

    filter_horizontal = (
        'groups', 'user_permissions', 'trophies',
    )

    @staticmethod
    def avatar_as_picture(obj):
        return mark_safe('<img src="{url}" width="{width}" height="{height}" style="border-radius:50%"/>'.format(
            url=obj.avatar.url,
            width=obj.avatar.width,
            height=obj.avatar.height,
        )
        )

    def get_readonly_fields(self, request, obj=None):
        extra = ()
        if obj:
            extra = ('avatar_as_picture',)
        return super().get_readonly_fields(request, obj) + extra
