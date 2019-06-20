from django.db.models import ExpressionWrapper, BooleanField, Q, Value
from rest_framework import viewsets

from ..serializer.entry_serializer import Entry, EntrySerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.filter(readability=True)
    serializer_class = EntrySerializer

    def get_queryset(self):
        user = self.request.user
        return Entry.objects.prefetch_related('likers', 'dislikers', 'favers').annotate(
            liked=ExpressionWrapper(Q(likers__id=user.id or 1), output_field=BooleanField()),
            disliked=ExpressionWrapper(Q(dislikers__id=user.id or 1), output_field=BooleanField()),
            faved=ExpressionWrapper(Q(favers__id=user.id or 1), output_field=BooleanField()),
        )
