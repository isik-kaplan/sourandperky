from django_filters import rest_framework as filters

from apps.sour_and_perky.models import User


class UserFilter(filters.FilterSet):
    class Meta:
        model = User
        fields = {
            'is_active': ['exact'],
            'is_staff': ['exact'],
            'is_superuser': ['exact'],
        }
