# Generated by Django 5.2 on 2025-06-29 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ai", "0002_20250629_1339"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aisettings",
            name="active_model",
            field=models.TextField(
                choices=[("deepseek/deepseek-chat-v3-0324", " ")],
                default="deepseek/deepseek-chat-v3-0324",
            ),
        ),
    ]
