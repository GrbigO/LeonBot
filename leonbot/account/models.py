from django.db import models
from django.contrib.postgres.fields import ArrayField



class User(models.Model):
	name = models.CharField(max_length=100)

	id = models.SmallIntegerField(max_length=50, db_index=True, null=True)
	username = models.CharField(max_length=200, blank=True)

	pv_log = ArrayField(base_field=models.JSONField(default=dict), default=list)
	deep = models.CharField(max_length=1000, blank=True)