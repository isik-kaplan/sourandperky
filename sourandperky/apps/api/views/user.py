from rest_framework import viewsets

from ..serializer.user_serializer import UserSerializer, User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
