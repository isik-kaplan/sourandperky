from django.contrib import admin

from .common import CommonAdmin
from ..models import UserTrophy


@admin.register(UserTrophy)
class UserTrophyAdmin(CommonAdmin):
    ...
