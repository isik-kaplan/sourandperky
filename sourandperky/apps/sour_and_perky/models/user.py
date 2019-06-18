from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import F, Count
from django.utils import timezone
from utils.models import field_image_from_link
# from utils.choices import Choices
from .common import CommonFields


class User(AbstractUser, CommonFields):
    # social
    favs = models.ManyToManyField('Entry', blank=True, related_name="favers")
    likes = models.ManyToManyField('Entry', blank=True, related_name="likers")
    dislikes = models.ManyToManyField('Entry', blank=True, related_name="dislikers")
    bio = models.TextField(max_length=1000, blank=True, null=True)
    trophies = models.ManyToManyField('UserTrophy', blank=True, related_name="owners")
    reported = models.ManyToManyField('Entry', blank=True, related_name='reported_by')
    followed_titles = models.ManyToManyField('Title', blank=True, related_name="followers")
    followed_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="followers")
    avatar = models.ImageField(blank=True, null=True, upload_to='avatars')

    # themes = Choices({
    #     'default': 'path_to_default_stylesheet'
    # })
    # theme = models.CharField()

    @property
    def liked_count(self):
        return self.entries.aggregate(Count(F('likers'))).get('likers__count', 0)

    @property
    def disliked_count(self):
        return self.entries.aggregate(Count(F('dislikers'))).get('dislikers__count', 0)

    @property
    def faved_count(self):
        return self.entries.aggregate(Count(F('favers'))).get('favers__count', 0)

    def random_avatar(self):
        AVATAR_URL = "https://api.adorable.io/avatars/{}{}"
        field_image_from_link(
            self,
            'avatar',
            '{}{}'.format(self.username, timezone.now()),
            AVATAR_URL.format(self.username, timezone.now().timestamp())
        )
        self.save()

    class Meta:
        ...
