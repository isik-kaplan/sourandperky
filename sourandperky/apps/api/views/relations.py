from django.http import Http404
from django.urls import path
from django_urls import UrlManager
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.routers import APIRootView
from rest_framework.views import APIView

from apps.sour_and_perky.models import Entry, User, Title
from utils.urls import url_mapping
from ..serializer import (
    EntryLikeSerializer,
    EntryDislikeSerializer,
    EntryFavSerializer,
    UserFollowSerializer,
    TitleFollowSerializer
)

relation_urls = UrlManager()


def relation_add_remove(model):
    class GenericRelationAddRemoveMixin:
        """@DynamicAttrs."""

        permission_classes = (IsAuthenticated,)

        @staticmethod
        def get_object(pk):
            try:
                return model.objects.get(pk=pk)
            except model.DoesNotExist:
                raise Http404

        def post(self, request, format=None):
            serializer = self.serializer_class(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.add_relations()
            return Response(status=status.HTTP_204_NO_CONTENT)

        def delete(self, request, format=None):
            serializer = self.serializer_class(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.remove_relations()
            return Response(status=status.HTTP_204_NO_CONTENT)

    return GenericRelationAddRemoveMixin


@relation_urls.path('like_entry/', name='like_entry')
class LikeEntryView(relation_add_remove(Entry), APIView):
    serializer_class = EntryLikeSerializer


@relation_urls.path('dislike_entry/', name='dislike_entry')
class DislikeEntryView(relation_add_remove(Entry), APIView):
    serializer_class = EntryDislikeSerializer


@relation_urls.path('fav_entry/', name='fav_entry')
class FavEntryView(relation_add_remove(Entry), APIView):
    serializer_class = EntryFavSerializer


@relation_urls.path('follow_user/', name='follow_user')
class FollowUserView(relation_add_remove(User), APIView):
    serializer_class = UserFollowSerializer


@relation_urls.path('follow_title/', name='follow_title')
class FollowTitleView(relation_add_remove(Title), APIView):
    serializer_class = TitleFollowSerializer


url_mapping_for_relations = url_mapping(relation_urls.url_patterns, 'api')

relation_urls.extend([
    path('', APIRootView.as_view(api_root_dict=url_mapping_for_relations), name='relations')
])
