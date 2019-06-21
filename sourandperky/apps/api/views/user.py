from rest_framework import viewsets

from apps.sour_and_perky.models import User
from ..filters import UserFilter
from ..serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter
    search_fields = ['username', 'first_name', 'last_name']
