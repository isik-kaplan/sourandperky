from django.db.models import Q, ExpressionWrapper, BooleanField
from django.utils import timezone
from rest_framework import viewsets

from ..filters.event import EventFilter
from ..serializer.event_serializer import Event, EventSerializer


class EventViewSet(viewsets.ModelViewSet):
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
