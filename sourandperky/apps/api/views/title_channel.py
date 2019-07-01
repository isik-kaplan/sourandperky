from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.sour_and_perky.models import TitleChannel
from ..filters import TitleChannelFilter
from ..serializer import TitleChannelSerializer


class TitleChannelViewSet(ReadOnlyModelViewSet):
    queryset = TitleChannel.objects.all()
    serializer_class = TitleChannelSerializer
    filterset_class = TitleChannelFilter
