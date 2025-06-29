from django.db import models

from .plugins.button import ButtonSort



class Plugin3Button(models.Model):
	button_sort = models.PositiveSmallIntegerField(choices=ButtonSort.CHOICES)
	buttons = models.TextField()
