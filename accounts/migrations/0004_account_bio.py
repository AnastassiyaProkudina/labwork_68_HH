# Generated by Django 4.2 on 2023-04-16 05:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0003_alter_account_avatar"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="bio",
            field=models.TextField(
                blank=True, verbose_name="Информация о пользователе"
            ),
        ),
    ]
