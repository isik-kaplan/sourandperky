from django.db.models import Count, Q, ExpressionWrapper, BooleanField

from apps.sour_and_perky.models import Title
from .common import NotDeletableViewSet
from ..filters import TitleFilter
from ..paginations import custom_paginator
from ..serializer import TitleSerializer


class TitleViewSet(NotDeletableViewSet):
    queryset = Title.objects.annotate(hre=Count('entries')).filter(hre__gt=0)
    serializer_class = TitleSerializer

    def get_queryset(self):
        return super().get_queryset().annotate(
            following=ExpressionWrapper(Q(followers__id=self.request.user.id or 1), BooleanField())
        )

    filterset_class = TitleFilter
    search_fields = ['text']
    pagination_class = custom_paginator()
