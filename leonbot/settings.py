import os
from typing import NoReturn, Any, Callable

from django.utils.module_loading import import_string
from dotenv import load_dotenv
import dj_database_url

from django.db.utils import DEFAULT_DB_ALIAS, ProgrammingError
from django.conf import global_settings

load_dotenv()


def empty() -> NoReturn:
	pass


def get_env(
		key: str,
		default: Any = empty,
) -> str | Any:
	try:
		value = os.environ[key]
	except KeyError:
		if default is empty:
			raise ValueError(f"{key} is not defined")

		value = default

	return value


def to_list(text: str):
	return [name.strip() for name in text.split(",") if name]



PROJECT_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))

DEBUG = False
ALLOWED_HOSTS = ["*"]
SECRET_KEY = None

AI_MODEL_NAME = "leonai"
AI_KEY = get_env("AI_KEY", None)
OPENROUTER_PROVISION_KEY = get_env("OPENROUTER_PROVISION_KEY")

TOKEN_BOT = get_env("TOKEN_BOT", None)
GROUP_ID = int(get_env("GROUP_ID"))

BOT_SETTING_PATH = get_env("BOT_SETTING_PATH", None)
BAD_USER = get_env("BAD_USER", None)


HOW_IM = get_env("HOW_IM", None)

if not BAD_USER is None:
	BAD_USER = set(to_list(BAD_USER))

INSTALLED_APPS = [
	"leonbot.account",
	"leonbot.core",
	"leonbot.ai",
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

if GROUP_ID is None:
	N = NotImplemented

if AI_KEY is None:
	N = NotImplemented
