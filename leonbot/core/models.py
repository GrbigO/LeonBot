from django.db import models

from leonbot.ai.models import AI

class Description(models.Model):
	description0 = models.TextField(blank=True)
	description1 = models.TextField(blank=True)
	description2 = models.TextField(blank=True)
	description3 = models.TextField(blank=True)

