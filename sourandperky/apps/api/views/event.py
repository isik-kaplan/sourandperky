from django.db.models import Q, ExpressionWrapper, BooleanField
from django.utils import timezone

from apps.sour_and_perky.models import Event
from .common import NotDeletableViewSet
from ..filters import EventFilter
from ..paginations import custom_paginator
from ..serializer import EventSerializer


class EventViewSet(NotDeletableViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self):
        return super().get_queryset().annotate(
            is_active=ExpressionWrapper(
                Q(start_date__lt=timezone.now()) & Q(end_date__gt=timezone.now()),
                output_field=BooleanField()
            ),
        )

    filterset_class = EventFilter

    search_fields = ['name', 'short_desc', 'desc']

    pagination_class = custom_paginator()
