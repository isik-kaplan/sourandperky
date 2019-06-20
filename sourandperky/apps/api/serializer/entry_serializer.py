from rest_framework import serializers

from apps.sour_and_perky.models import Entry
from .conditional_serializer import ConditionalSerializerMixin
from .title_serializer import TitleSerializer
from .user_serializer import UserSerializer


class EntrySerializer(ConditionalSerializerMixin, serializers.ModelSerializer):
    liked = serializers.SerializerMethodField('is_liked', read_only=True)
    disliked = serializers.SerializerMethodField('is_disliked', read_only=True)
    faved = serializers.SerializerMethodField('is_faved', read_only=True)
    author = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    @staticmethod
    def is_liked(obj):
        liked = getattr(obj, 'liked', False)
        return bool(liked)

    @staticmethod
    def is_disliked(obj):
        disliked = getattr(obj, 'disliked', False)
        return bool(disliked)

    @staticmethod
    def is_faved(obj):
        faved = getattr(obj, 'faved', False)
        return bool(faved)

    class Meta:
        model = Entry
        fields = [
            'timestamp',
            'id',
            'title',
            'text',
            'liked',
            'disliked',
            'faved',
            'author'
        ]
        conditional_fields = [
            'author',
            'title',
        ]
        relational_fields = {
            'title': lambda: TitleSerializer(read_only=True),
            'author': lambda: UserSerializer(read_only=True, default=serializers.CurrentUserDefault()),
        }
