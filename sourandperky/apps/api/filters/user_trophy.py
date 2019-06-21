from django_filters import rest_framework as filters

from apps.sour_and_perky.models import UserTrophy


class UserTrophyFilter(filters.FilterSet):
    class Meta:
        model = UserTrophy
        fields = {}
