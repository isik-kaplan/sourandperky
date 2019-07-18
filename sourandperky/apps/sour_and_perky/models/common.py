import uuid

from django.contrib.auth import get_user_model
from django.db import models
from simple_history.models import HistoricalRecords


def _first_user_id(cache={'user': None}):
    def function():
        if cache['user']:
            return cache['user'].id
        else:
            cache['user'] = get_user_model().objects.order_by('timestamp').first()
            return cache['user'].id

    return function


first_user_id = _first_user_id()


class CommonFields(models.Model):
    # fields
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # managers
    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True
