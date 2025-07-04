# Generated by Django 5.2 on 2025-06-24 15:37

import django.contrib.postgres.fields
import functools
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AISettings",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "msg_logs",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.JSONField(default=dict),
                        default=functools.partial(list, *(dict,), **{}),
                        size=None,
                    ),
                ),
                ("deep", models.CharField(blank=True, max_length=1000)),
                ("active_model", models.TextField(choices=[("", "none")], default="")),
                ("stores", models.JSONField(default=dict)),
                ("update_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
