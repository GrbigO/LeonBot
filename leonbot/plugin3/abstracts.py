from django.db import models

class ModelWithPluginInstaller(models.Model):

	class Meta:
		abstract = True