from django.db.models import Count
from rest_framework import viewsets

from ..filters.title import TitleFilter
from ..serializer.title_serializer import Title, TitleSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(hre=Count('entries')).filter(hre__gt=0)
    serializer_class = TitleSerializer
    filterset_class = TitleFilter
    search_fields = ['text']
