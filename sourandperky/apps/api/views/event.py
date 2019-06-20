from rest_framework import viewsets

from ..serializer.event_serializer import Event, EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
