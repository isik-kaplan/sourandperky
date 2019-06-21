from django_filters import rest_framework as filters

from apps.sour_and_perky.models import Event


class EventFilter(filters.FilterSet):
    is_active = filters.BooleanFilter(field_name='is_active')

    @staticmethod
    def get_is_active(obj):
        return obj.is_active

    class Meta:
        model = Event
        fields = {
            'is_active': ['exact']
        }
