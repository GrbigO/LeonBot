import os
from typing import NoReturn, Any, Callable


from django.db.utils import DEFAULT_DB_ALIAS, ProgrammingError
from django.conf import global_settings



def empty() -> NoReturn:
    raise

def get_env(
    key: str,
    default: Any = empty,
    type_conversion: empty | Callable[..., ...] = empty,
) -> str | Any:
    try:
        value = os.environ[key]

    except KeyError:
        if default is empty:
            raise ValueError(f"{key} is not defined")

        value = default

    if type_conversion is empty:
        return value
    try:
        return type_conversion(value)
    except (AttributeError, ValueError, TypeError, NameError) as exp:
        raise ProgrammingError(f"{exp}") from exp



PROJECT_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))


DEBUG = False
ALLOWED_HOSTS = ["*"]
SECRET_KEY = None



INSTALLED_APPS = [
    "leonbot.conf"
]

MIDDLEWARE = ["django.middleware.security.SecurityMiddleware"]
ROOT_URLCONF = ""
WSGI_APPLICATION = ""
AUTH_PASSWORD_VALIDATORS = []


DATABASES = {
    DEFAULT_DB_ALIAS: {
    }
}


LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

AI_MODEL_NAME = "leon-ai"
AI_TEXT_TRAIN_PATH: str = "C:\\Users\\Mohammad\\Desktop\\amozesh_qam_for_amirkhande.txt"
GPT2_TOKENNIZER_PATH: str = "D:\\Ashkan\\model"
GPT2_LMHEADMODEL_PATH: str = "D:\\Ashkan\\model"