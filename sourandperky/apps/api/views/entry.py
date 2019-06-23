from django.db.models import ExpressionWrapper, BooleanField, Q, Count, F
from rest_framework import viewsets

from apps.sour_and_perky.models import Entry
from ..filters import EntryFilter
from ..serializer import EntrySerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

    def get_queryset(self):
        user = self.request.user
        return Entry.objects.prefetch_related('likers', 'dislikers', 'favers').annotate(
            liked=ExpressionWrapper(Q(likers__id=user.id or 1), output_field=BooleanField()),
            disliked=ExpressionWrapper(Q(dislikers__id=user.id or 1), output_field=BooleanField()),
            faved=ExpressionWrapper(Q(favers__id=user.id or 1), output_field=BooleanField()),
            points=Count(F('likers'), distinct=True) - Count(F('dislikers'), distinct=True),
        )

    filterset_class = EntryFilter

    search_fields = ['text']

    ordering_fields = ['points', 'timestamp']
