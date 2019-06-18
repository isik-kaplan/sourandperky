from django.db.models import signals
from django.dispatch import receiver

from utils.models import field_image_from_link
from ..models import User


@receiver(signals.pre_save, sender=User)
def add_user_profile_picture(**kwargs):
    AVATAR_URL = "https://api.adorable.io/avatars/{}"
    instance = kwargs['instance']
    if not instance.avatar:
        field_image_from_link(
            instance,
            'avatar',
            '{}...{}'.format(instance.username, instance.id),
            AVATAR_URL.format(instance.id)
        )
