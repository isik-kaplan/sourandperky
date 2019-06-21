from rest_framework import viewsets

from ..filters.user_trophy import UserTrophyFilter
from ..serializer.user_trophy_serializer import UserTrophySerializer, UserTrophy


class UserTrophyViewSet(viewsets.ModelViewSet):
    queryset = UserTrophy.objects.all()
    serializer_class = UserTrophySerializer
    filterset_class = UserTrophyFilter
