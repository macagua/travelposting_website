# Generated by Django 2.1.11 on 2020-09-02 22:57

import apps.destinations.formatChecker
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directmessages', '0003_auto_20200707_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='image',
            field=apps.destinations.formatChecker.ContentTypeRestrictedFileField(blank=True, null=True, upload_to='file_image/'),
        ),
    ]