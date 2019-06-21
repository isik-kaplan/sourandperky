from django.db.models import Count
from rest_framework import viewsets

from apps.sour_and_perky.models import Title
from ..filters import TitleFilter
from ..serializer import TitleSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(hre=Count('entries')).filter(hre__gt=0)
    serializer_class = TitleSerializer
    filterset_class = TitleFilter
    search_fields = ['text']
