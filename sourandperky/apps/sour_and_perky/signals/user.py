from django.db.models import signals
from django.dispatch import receiver

from ..models import User


@receiver(signals.pre_save, sender=User)
def add_user_profile_picture(**kwargs):
    instance = kwargs['instance']
    if not instance.avatar:
        instance.random_avatar()
