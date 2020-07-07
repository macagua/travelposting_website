# Generated by Django 2.1.11 on 2020-07-07 13:43

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0011_contactus'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactus',
            options={'verbose_name': 'Contacts', 'verbose_name_plural': 'Contact Us'},
        ),
        migrations.AlterField(
            model_name='contactus',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='message',
            field=models.CharField(max_length=300, verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AlterField(
            model_name='magazine',
            name='files',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=False, related_name='file_magazine', to=settings.FILER_IMAGE_MODEL, verbose_name='Files'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='paypal_id',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Paypal ID'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AlterField(
            model_name='planfeature',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='planfeature',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AlterField(
            model_name='price',
            name='type',
            field=models.ForeignKey(on_delete=None, to='landing_page.PriceType', verbose_name='Price Type'),
        ),
        migrations.AlterField(
            model_name='privacysetting',
            name='pinteres',
            field=models.BooleanField(default=True, verbose_name='Pinterest'),
        ),
        migrations.AlterField(
            model_name='service',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='service',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AlterField(
            model_name='testimony',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='testimony',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
    ]
