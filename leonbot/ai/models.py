from django.db import models
from django.conf import settings

from leonbot.core.models import ModelWithDescriptions, ModelWithDateTime


class AI(ModelWithDescriptions, ModelWithDateTime):
	name = models.CharField(max_length=50, primary_key=True, null=False, editable=False, serialize=False)
	key = models.CharField(max_length=120)
	msgs = models.JSONField(default=dict)

	created_by = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="created_by")
	updated_by = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="updated_by")

	class Meta:
		db_table = "ai_model"

	def get_description(self) -> set[str]:
		return {
			self.description0,
			self.description1,
			self.description2,
			self.description3,
		}


def update_msg(user_value, ai_value, old_values):
	return NotImplemented