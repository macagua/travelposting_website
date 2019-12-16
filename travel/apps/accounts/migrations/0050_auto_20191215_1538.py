# Generated by Django 2.1.12 on 2019-12-15 19:38

import apps.accounts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0034_auto_20191108_1614'),
        ('accounts', '0049_auto_20191214_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='accounts.Comment')),
                ('post', models.ForeignKey(on_delete=None, related_name='comments', to='destinations.Destination')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.AlterModelManagers(
            name='customeruser',
            managers=[
                ('objects', apps.accounts.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='user_answer',
            field=models.ForeignKey(max_length=80, on_delete=django.db.models.deletion.CASCADE, related_name='user_answer_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_comment',
            field=models.ForeignKey(max_length=80, on_delete=django.db.models.deletion.CASCADE, related_name='user_comment_to', to=settings.AUTH_USER_MODEL),
        ),
    ]
