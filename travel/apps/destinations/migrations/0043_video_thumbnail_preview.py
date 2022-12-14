# Generated by Django 2.1.11 on 2020-07-27 03:07

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0042_auto_20200726_0124'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='thumbnail_preview',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='gallery/thumbnail/', verbose_name='Thumbnail'),
        ),
    ]
