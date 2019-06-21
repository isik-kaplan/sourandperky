from django_filters import rest_framework as filters

from apps.sour_and_perky.models import Entry


class EntryFilter(filters.FilterSet):
    class Meta:
        model = Entry
        fields = {
            'author': ['exact'],
            'readability': ['exact'],
            'title': ['exact']
        }
