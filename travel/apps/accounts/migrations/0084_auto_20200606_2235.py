# Generated by Django 2.1.11 on 2020-06-07 02:35

from django.db import migrations, models
from django.utils.text import slugify

import apps.accounts.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0083_auto_20200531_1909'),
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
            name='slug',
            field=models.SlugField(null=True, max_length=200),
            preserve_default=False,
        )
    ]
