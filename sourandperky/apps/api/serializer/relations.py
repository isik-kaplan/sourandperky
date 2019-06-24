from rest_framework import serializers

from apps.sour_and_perky.models import Entry, Title, User


def primary_key_related(model):
    class PrimaryKeyRelated(serializers.PrimaryKeyRelatedField):
        def get_queryset(self):
            return model.objects.all()

    PrimaryKeyRelated.__name__ = model.__name__ + PrimaryKeyRelated.__name__

    return PrimaryKeyRelated()


class Common(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())


class EntryLikeSerializer(Common):
    entry = primary_key_related(Entry)

    def add_relations(self):
        user = self.context['request'].user
        entry = self.validated_data.pop('entry')
        user.like_entry(entry)

    def remove_relations(self):
        user = self.context['request'].user
        entry = self.validated_data.pop('entry')
        user.remove_entry_like(entry)


class EntryDislikeSerializer(Common):
    entry = primary_key_related(Entry)

    def add_relations(self):
        user = self.context['request'].user
        entry = self.validated_data.pop('entry')
        user.dislike_entry(entry)

    def remove_relations(self):
        user = self.context['request'].user
        entry = self.validated_data.pop('entry')
        user.remove_entry_dislike(entry)


class EntryFavSerializer(Common):
    entry = primary_key_related(Entry)

    def add_relations(self):
        user = self.context['request'].user
        entry = self.validated_data.pop('entry')
        user.fav_entry(entry)

    def remove_relations(self):
        user = self.context['request'].user
        entry = self.validated_data.pop('entry')
        user.remove_entry_fav(entry)


class UserFollowSerializer(Common):
    targer_user = primary_key_related(User)

    def add_relations(self):
        user = self.context['request'].user
        target_user = self.validated_data.pop('target_user')
        user.follow_user(target_user)

    def remove_relations(self):
        user = self.context['request'].user
        target_user = self.validated_data.pop('target_user')
        user.unfollow_user(target_user)


class TitleFollowSerializer(Common):
    title = primary_key_related(Title)

    def add_relations(self):
        user = self.context['request'].user
        title = self.validated_data.pop('title')
        user.follow_title(title)

    def remove_relations(self):
        user = self.context['request'].user
        title = self.validated_data.pop('title')
        user.unfollow_title(title)
