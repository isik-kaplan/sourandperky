from rest_framework import viewsets

from apps.sour_and_perky.models import TitleChannel
from ..filters import TitleChannelFilter
from ..serializer import TitleChannelSerializer


class TitleChannelViewSet(viewsets.ModelViewSet):
    queryset = TitleChannel.objects.all()
    serializer_class = TitleChannelSerializer
    filterset_class = TitleChannelFilter
