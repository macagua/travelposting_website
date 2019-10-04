# Generated by Django 2.1.12 on 2019-10-03 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0016_destination_is_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_description', models.CharField(max_length=50, verbose_name='Short Description')),
                ('detail_itinerary', models.TextField(verbose_name='Detail Itinerary')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destinations.Destination', verbose_name='Itinerary')),
                ('option_tab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destinations.OptionTabData', verbose_name='Option tab')),
            ],
        ),
    ]