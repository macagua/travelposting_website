# Generated by Django 2.1.14 on 2020-01-08 03:37

import apps.accounts.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0072_auto_20200104_0918'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customeruser',
            managers=[
                ('objects', apps.accounts.models.UserManager()),
            ],
        ),
    ]
