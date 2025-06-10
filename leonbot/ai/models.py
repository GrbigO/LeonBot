from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField

from ..core.models import ModelWithBasicField



class AI(ModelWithBasicField):

	id = models.IntegerField(primary_key=True)
	stores = models.JSONField(default=dict)

	users = models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True, related_name="ai_models")

	NAME = "Leon AI"
	VERSION = "v1"

	class Meta:
		db_table = "ai_model"
