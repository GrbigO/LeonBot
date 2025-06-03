from django.db import models
from django.conf import settings



class AI(models.Model):
	name = models.CharField(max_length=50, primary_key=True, null=False, editable=False, serialize=False)
	model = models.CharField(max_length=100)
	key = models.CharField(max_length=120)
	msgs = models.JSONField()


	descriptions = models.OneToOneField(to="core.Description", on_delete=models.CASCADE)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	created_by = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="created_by")
	updated_by = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="updated_by")


