# Generated by Django 5.2 on 2025-06-24 16:21

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("ai", "0001_initial"),
        ("permission", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BOT",
            fields=[
                (
                    "telegram_id",
                    models.CharField(max_length=45, primary_key=True, serialize=False),
                ),
                ("settings", models.JSONField(default=dict)),
                ("last_used", models.DateField(default=django.utils.timezone.now)),
                (
                    "ai",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="ai.aisettings"
                    ),
                ),
                (
                    "bot_access",
                    models.ManyToManyField(
                        blank=True,
                        related_name="bot_set",
                        related_query_name="bot",
                        to="permission.permission",
                    ),
                ),
                (
                    "prent",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bot.bot",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
