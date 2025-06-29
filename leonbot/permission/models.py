from django.db import models


class Permission(models.Model):
    codename = models.CharField(max_length=100)


class PermissionsMixin(models.Model):

    accesses = models.ManyToManyField(
        Permission,
        blank=True,
        related_name="bot_set",
        related_query_name="bot",
    )

    class Meta:
        abstract = True

