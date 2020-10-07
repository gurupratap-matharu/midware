import uuid

from django.db import models


class Request(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    body = models.CharField(max_length=5000, blank=True)
