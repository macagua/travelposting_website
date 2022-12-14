# Generated by Django 2.1.12 on 2019-12-10 02:56

import apps.accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0044_auto_20191209_2119'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customeruser',
            managers=[
                ('objects', apps.accounts.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='customeruser',
            name='is_community',
            field=models.BooleanField(default=True),
        ),
    ]
