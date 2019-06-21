from django_filters import rest_framework as filters

from apps.sour_and_perky.models import TitleChannel


class TitleChannelFilter(filters.FilterSet):
    class Meta:
        model = TitleChannel
        fields = {}
