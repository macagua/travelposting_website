# Generated by Django 2.1.11 on 2020-06-05 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0039_messagedashboard'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messagedashboard',
            name='recipient',
        ),
    ]
