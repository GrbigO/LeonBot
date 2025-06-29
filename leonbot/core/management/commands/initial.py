from django.conf import settings
from django.core.management.base import BaseCommand


from ....bot.models import BOT
from ....ai.models import AISettings


class Command(BaseCommand):
	help = ""

	def add_arguments(self, parser):
		parser.add_argument(
			"--again",
			action="store_true",
			help="Use this flag to reinitialize the bot if it already exists.",
		)

	def handle(self, **options):
		# first check if you...
		mybot = BOT.objects.filter(telegram_id="1").first()
		if mybot:
			reload = options.get("again", False)
			if not reload:
				self.stdout.write(self.style.ERROR(
					"Your bot is already registered. For reset the bot, inter:\n"
					".\\manage.py bot --again"
				))
				return

			mybot.delete()

		my_ai_settings = AISettings.objects.create()

		bot_id = "1"
		my_bot = BOT.objects.create(telegram_id=bot_id, ai=my_ai_settings)

