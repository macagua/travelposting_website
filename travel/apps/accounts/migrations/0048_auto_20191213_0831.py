# Generated by Django 2.1.12 on 2019-12-13 12:31

import apps.accounts.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0047_auto_20191212_0053'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customeruser',
            managers=[
                ('objects', apps.accounts.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='customeruser',
            name='following',
            field=models.ManyToManyField(related_name='followers', through='accounts.Contact', to=settings.AUTH_USER_MODEL),
        ),
    ]
