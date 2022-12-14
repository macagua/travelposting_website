# Generated by Django 2.1.11 on 2020-05-31 23:09

import apps.accounts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0082_auto_20200515_1253'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastVisitIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_ip_login', models.GenericIPAddressField(blank=True, null=True, protocol='IPv4', verbose_name='Last Login')),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.AlterModelManagers(
            name='customeruser',
            managers=[
                ('objects', apps.accounts.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='customeruser',
            name='last_ip',
            field=models.GenericIPAddressField(blank=True, null=True, protocol='IPv4', verbose_name='Last Login IP'),
        ),
        migrations.AddField(
            model_name='customeruser',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='lastvisitip',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
