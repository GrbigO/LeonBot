from django.db import models


class ModelWithDescriptions(models.Model):
	description0 = models.TextField(blank=True)
	description1 = models.TextField(blank=True)
	description2 = models.TextField(blank=True)
	description3 = models.TextField(blank=True)

	class Meta:
		abstract = True

class ModelWithDateTime(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True