from rest_framework import viewsets

from ..filters.title_channel import TitleChannelFilter
from ..serializer.title_channel_serializer import TitleChannel, TitleChannelSerializer


class TitleChannelViewSet(viewsets.ModelViewSet):
    queryset = TitleChannel.objects.all()
    serializer_class = TitleChannelSerializer
    filterset_class = TitleChannelFilter
