from apps.sour_and_perky.models import TitleChannel
from .common import NotDeletableViewSet
from ..filters import TitleChannelFilter
from ..serializer import TitleChannelSerializer


class TitleChannelViewSet(NotDeletableViewSet):
    queryset = TitleChannel.objects.all()
    serializer_class = TitleChannelSerializer
    filterset_class = TitleChannelFilter
