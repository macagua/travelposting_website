# Generated by Django 2.1.12 on 2019-09-15 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0003_magazine'),
    ]

    operations = [
        migrations.RenameField(
            model_name='magazine',
            old_name='estatus',
            new_name='status',
        ),
    ]
