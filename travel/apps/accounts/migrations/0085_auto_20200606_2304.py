# Generated by Django 2.1.11 on 2020-06-07 03:04

from django.db import migrations, models
from django.utils.text import slugify

from random import randint
import uuid


def add_slug(apps, schema_editor):
    User = apps.get_model('accounts', 'CustomerUser')
    for user in User.objects.all():
        name = '{} {}'.format(user.first_name, user.last_name) if not user.business_name else user.business_name
        name = name if name.strip() != '' else  uuid.uuid4()
        slug = slugify(name)
        if User.objects.filter(slug=slug).exists():
            slug = slugify(name+"-"+str(randint(300,999)))
        user.slug = slug
        user.save()

def remove_slug(apps, schema_editor):
    User = apps.get_model('accounts', 'CustomerUser')
    User.objects.all().exclude(slug=None).update(slug=None)

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0084_auto_20200606_2235'),
    ]

    operations = [
        migrations.RunPython(add_slug, remove_slug),
        ]
