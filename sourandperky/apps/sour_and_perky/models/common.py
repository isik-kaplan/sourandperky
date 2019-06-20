import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords


def first_user_id(cache={'user': None}):
    if cache['user']:
        return cache['user'].id
    else:
        cache['user'] = get_user_model().objects.order_by('timestamp').first()
        return cache['user'].id


class CommonFields(models.Model):
    # fields
    timestamp = models.DateTimeField(default=timezone.now, db_index=True, editable=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # managers
    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True
