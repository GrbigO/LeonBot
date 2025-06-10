from django.core.management.base import BaseCommand
from django.conf import settings

from ....account.models import User
from ....ai.models import AI


class Command(BaseCommand):

	def handle(self, *args, **options):
		User.objects.all().delete()
		AI.objects.all().delete()
		leon_mamber = [
			{"name": "استاد", "la_qab": "", "username": "559808099"},
			{"name": "سومکا", "la_qab": "سیاه پوست", "username": "SUMKA85"},
			{"name": "ازی", "la_qab": "گون ساما بوب", "username": "5657121075"},
			{"name": "مهدی پاگ", "la_qab": "تک رو( کله ماهی)", "username": "961127922"},
			{"name": "فمبوی حرفه ای", "la_qab": "امیر پرعکس", "username": "787066596"},
			{"name": "فیاض", "la_qab": "بکن امیرفان / شنتاو، مسی فن", "username": "7527404770"},
			{"name": "جوجو", "la_qab": "لاشئ اعظم", "username": "Sleepy_hmm"},
			{"name": "امیر فان", "la_qab": "عرق خور", "username": "1973509615"},
			{"name": "شیلنگ", "la_qab": "شیلنگ", "username": "Shahang_g"},
			{"name": "سفید پوست", "la_qab": "توسلا", "username": "SoryuQQ"},
			{"name": "ناشناس", "la_qab": "آتو مخستر", "username": ""},
			{"name": "شیرازی کون گشاد اسم: سینا", "la_qab": "گشاد", "username": "1535849516"},
			{"name": "سروش", "la_qab": "زیرکش (فاقد لقب)", "username": "828728619"},
			{"name": "دادوی", "la_qab": "مدگل", "username": "6917725218"},
			{"name": "سگ عراق اسم: پارسا", "la_qab": "FBI جاسوس", "username": "349889388"},
			{"name": "شایان", "la_qab": "جنگ ستارگان فن", "username": "Shyanof"},
			{"name": "کصخلی که فقط گیف میفرسه اسم: ایمه", "la_qab": "آیتمه", "username": "Ashil_AM"},
			{"name": "نمیدونم کی هستم", "la_qab": "ناشناس", "username": ""},
			{"name": "مهدی منظومه", "la_qab": "پشه فضایی / کرجی", "username": "mahdi47x"},
			{"name": "اواز خون کصمشنگ", "la_qab": "حق گو عظیم / مرده", "username": "Benii85_najafi"},
		]
		users = []
		for mmber in leon_mamber:
			users.append(User(**mmber))
		User.objects.bulk_create(users)

		created_by = User.objects.get(name="استاد")
		AI.objects.create(
			name=settings.AI_MODEL_NAME, key=settings.AI_KEY, created_by=created_by, updated_by=created_by,
			description0=settings.GROUP_INFORMATION0,
			description1=settings.GROUP_INFORMATION1,
			description2=settings.GROUP_INFORMATION2,
			description3=settings.GROUP_INFORMATION3,
		)
