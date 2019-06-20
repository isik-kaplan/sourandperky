from rest_framework import viewsets

from ..serializer.user_trophy_serializer import UserTrophySerializer, UserTrophy


class UserTrophyViewSet(viewsets.ModelViewSet):
    queryset = UserTrophy.objects.all()
    serializer_class = UserTrophySerializer
