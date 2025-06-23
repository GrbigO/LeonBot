import os
from typing import Any


import dj_database_url
from django.utils.module_loading import import_string
from dotenv import load_dotenv


from django.utils.functional import empty
from django.db.utils import DEFAULT_DB_ALIAS
from django.conf import global_settings




load_dotenv()



def get_env(key: str, default: Any = empty) -> str | Any:
	try:
		value = os.environ[key]
	except KeyError:
		if default is empty:
			raise ValueError(f"{key} is not defined")

		value = default

	return value


def to_list(text: str):
	return [name.strip() for name in text.split(",") if name]


# api
API_ADDERS = "https://openrouter.ai/api/v1/chat/completions"

PROJECT_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))

DEBUG = False
ALLOWED_HOSTS = []
SECRET_KEY = None

API_KEY = get_env("API_KEY", None)
WEBHOOK_KEY = get_env("WEBHOOK_KEY", None)
OPENROUTER_PROVISION_KEY = get_env("OPENROUTER_PROVISION_KEY")


# learn how to ues rd.
BOT_SETTINGS = {
	"NAME": "Leon",
	"TOKEN_BOT": get_env("TOKEN_BOT", None),
	"REQUEST_NAME": get_env("REQUEST_NAME").split(","),

	"USERNAME": "@LE0NAI_bot",
	"GROUP_MAX_LENGTH": 8,
	"MAX_MSG_LOGS": int(get_env("MAX_MSG_LOGS", 200)),

	"START_MSG": "  If you don't know what this bot is for,\n"
				 "  what it does,\n"
				 "  or how to use it,\n"
				 "  select the -Help- option.\n"
}


INSTALLED_APPS = [
	# Django modules
	"django.contrib.contenttypes",
	"django.contrib.postgres",
	# Local apps
	"leonbot.bot",
	"leonbot.ai",
	"leonbot.permission",
	"leonbot.plugin3",
]

MIDDLEWARE = []
AUTH_USER_MODEL = "account.User"
ROOT_URLCONF = ""
WSGI_APPLICATION = ""
AUTH_PASSWORD_VALIDATORS = []
AUTHENTICATION_BACKENDS = [""]

DATABASES = {
	DEFAULT_DB_ALIAS: dj_database_url.parse(get_env("DATABASE_URL")),
}

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# if GROUP_ID is None:


# if API_KEY is None:
