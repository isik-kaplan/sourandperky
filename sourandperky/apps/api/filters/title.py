from django_filters import rest_framework as filters

from apps.sour_and_perky.models import Title


class TitleFilter(filters.FilterSet):
    class Meta:
        model = Title
        fields = {
            'creator': ['exact'],
            'channels': ['contains']
        }
