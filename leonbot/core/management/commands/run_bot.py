from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        from .... import account
        from ... import bot_application
        pass

