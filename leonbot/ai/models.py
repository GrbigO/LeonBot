from django.db import models
from django.conf import settings

class AI(models.Model):
	name = models.CharField(max_length=50, primary_key=True, null=False, editable=False)
	key = models.CharField(max_length=120)

	descriptions = models.OneToOneField(to="core.Description", on_delete=models.CASCADE)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	created_by = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="created_by")
	updated_by = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="updated_by")




class AILog(models.Model):
	ai_name = models.CharField(max_length=50)
	msg = models.JSONField()
	data = models.DateTimeField(auto_now=True)


