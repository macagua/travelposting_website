# Generated by Django 2.1.12 on 2019-11-08 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0033_auto_20191107_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destinationvisitor',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visitor', to='destinations.Destination'),
        ),
    ]
