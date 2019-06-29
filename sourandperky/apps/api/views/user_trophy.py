from rest_framework import viewsets

from apps.sour_and_perky.models import UserTrophy
from ..filters import UserTrophyFilter
from ..serializer import UserTrophySerializer


class UserTrophyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserTrophy.objects.all()
    serializer_class = UserTrophySerializer
    filterset_class = UserTrophyFilter
