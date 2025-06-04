from django.db import models

class User(models.Model):

	name = models.CharField(max_length=100)
	la_qab = models.CharField(max_length=100)
	username = models.CharField(max_length=150 , blank=True)
	phone = models.CharField(max_length=15 , blank=True)

