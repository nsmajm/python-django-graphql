# Generated by Django 4.1.1 on 2022-09-26 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role_id',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]