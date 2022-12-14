# Generated by Django 2.1.12 on 2019-10-04 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0007_auto_20190927_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeleteReg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('agree', models.BooleanField(default=True, verbose_name='Agree?')),
                ('status', models.BooleanField(default=True, verbose_name='Status?')),
            ],
            options={
                'verbose_name': 'Delete Register',
                'verbose_name_plural': 'Delete Registers',
            },
        ),
    ]
