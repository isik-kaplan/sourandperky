from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

UpdateRetrieveListBases = (
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
)


class UpdateRetrieveListViewSet(*UpdateRetrieveListBases):
    ...
