# Generated by Django 2.1.15 on 2020-01-03 21:39

import apps.accounts.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0069_auto_20200103_1735'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customeruser',
            managers=[
                ('objects', apps.accounts.models.UserManager()),
            ],
        ),
    ]
