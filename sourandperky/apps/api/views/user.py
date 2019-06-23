from django.db.models import ExpressionWrapper, Q, BooleanField

from apps.sour_and_perky.models import User
from .common import UpdateRetrieveListViewSet
from ..filters import UserFilter
from ..permissions import IsCurrentUserOrReadOnly
from ..serializer import UserSerializer


class UserViewSet(UpdateRetrieveListViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return super().get_queryset().annotate(
            following=ExpressionWrapper(Q(followers__id=self.request.user.id or 1), BooleanField())
        )

    filterset_class = UserFilter
    search_fields = ['username', 'first_name', 'last_name']
    permission_classes = (IsCurrentUserOrReadOnly,)
