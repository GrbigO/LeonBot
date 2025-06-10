from django.db import models


from ..core.models import ModelWithBasicField


class User(ModelWithBasicField):
	id = models.IntegerField(primary_key=True)



