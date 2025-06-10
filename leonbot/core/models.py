from django.db import models
from django.contrib.postgres.fields import ArrayField


from . import AIChatModel
from ..botconfs import bot_settings


class ModelWithBasicField(models.Model):

	msg_logs = ArrayField(base_field=models.JSONField(default=dict), default=list)
	deep = models.CharField(max_length=1000, blank=True)
	active_model = models.CharField(max_length=150, default=AIChatModel.DEEPSEEK_v3_0324, choices=AIChatModel.Choice)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.updated_field = []


	class Meta:
		abstract = True


	def get_msg_logs(self):
		len_msg_logs = len(self.msg_logs)
		base_index = 0
		if len_msg_logs > bot_settings.MAX_MSG_LOGS:
			base_index = len_msg_logs - bot_settings.MAX_MSG_LOGS

			self.msg_logs = self.msg_logs[base_index + 2: len_msg_logs]
			self.updated_field.append("msg_logs")

		return self.msg_logs

