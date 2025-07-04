# Generated by Django 5.2 on 2025-06-29 13:39

import django.contrib.postgres.fields
import functools
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ai", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aisettings",
            name="msg_logs",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.JSONField(default=dict),
                default=functools.partial(list, *({},), **{}),
                size=None,
            ),
        ),
    ]
