# Generated by Django 2.1.12 on 2019-10-22 05:16

import apps.accounts.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0039_auto_20191021_1918'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customeruser',
            managers=[
                ('objects', apps.accounts.models.UserManager()),
            ],
        ),
    ]
