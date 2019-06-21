from rest_framework import viewsets

from ..filters.user import UserFilter
from ..serializer.user_serializer import UserSerializer, User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter
    search_fields = ['username', 'first_name', 'last_name']
