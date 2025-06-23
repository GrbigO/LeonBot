from django.db import models

from ..core.models import ModelWithAuthField
from ..plugin3.abstracts import ModelWithInstallPlugin


class BOT(ModelWithAuthField, ModelWithInstallPlugin):
	# user_id or group_id in telegram
	telegram_id = models.BigIntegerField(primary_key=True, serialize=False)
	ai = models.OneToOneField(to="ai.AISettings", on_delete=models.CASCADE)

	def add_new_log(self, log: dict) -> None:
		self.ai.msg_logs.append(log)
