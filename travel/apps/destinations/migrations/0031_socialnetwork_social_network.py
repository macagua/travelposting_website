# Generated by Django 2.1.12 on 2019-10-22 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0030_auto_20191021_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialnetwork',
            name='social_network',
            field=models.BooleanField(default=False, help_text='Check for use the network from user', verbose_name='Social Network'),
        ),
    ]
