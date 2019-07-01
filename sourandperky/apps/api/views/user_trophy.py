from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.sour_and_perky.models import UserTrophy
from ..filters import UserTrophyFilter
from ..serializer import UserTrophySerializer


class UserTrophyViewSet(ReadOnlyModelViewSet):
    queryset = UserTrophy.objects.all()
    serializer_class = UserTrophySerializer
    filterset_class = UserTrophyFilter
