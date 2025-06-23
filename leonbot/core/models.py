from django.db import models

class ModelWithAuthField(models.Model):
	last_used = models.DateField(auto_now=True)

	class Meta:
		abstract = True