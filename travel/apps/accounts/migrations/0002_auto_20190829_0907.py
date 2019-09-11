# Generated by Django 2.1.11 on 2019-08-29 09:07

import apps.accounts.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0001_initial'),
        ('auth', '0009_alter_user_last_name_max_length'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customeruser',
            managers=[
                ('objects', apps.accounts.models.UserManager()),
            ],
        ),
        migrations.RenameField(
            model_name='customeruser',
            old_name='is_admin',
            new_name='is_staff',
        ),
        migrations.RemoveField(
            model_name='customeruser',
            name='company_code',
        ),
        migrations.RemoveField(
            model_name='customeruser',
            name='username',
        ),
        migrations.AddField(
            model_name='customeruser',
            name='business_address',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Dirección comercial'),
        ),
        migrations.AddField(
            model_name='customeruser',
            name='business_name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Nombre de la empresa'),
        ),
        migrations.AddField(
            model_name='customeruser',
            name='business_position',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Cargo en la empresa'),
        ),
        migrations.AddField(
            model_name='customeruser',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='¿Tienen algo que decirnos?'),
        ),
        migrations.AddField(
            model_name='customeruser',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='País'),
        ),
        migrations.AddField(
            model_name='customeruser',
            name='coupon',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Coupon'),
        ),
        migrations.AddField(
            model_name='customeruser',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AddField(
            model_name='customeruser',
            name='degree',
            field=models.CharField(blank=True, choices=[('sra', 'Sra.'), ('sr', 'Sr.'), ('divers', 'Divers'), ('dr', 'Dr.'), ('prof', 'Prof.'), ('lic', 'Lic.'), ('agrupacion', 'Agrupación'), ('prof-dr', 'Prof. Dr.')], max_length=20, null=True, verbose_name='Título (Persona de contacto)'),
        ),
        migrations.AddField(
            model_name='customeruser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='customeruser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customeruser',
            name='language',
            field=models.CharField(choices=[('es', 'Spanish'), ('en', 'English'), ('de', 'German')], default='en', max_length=2, verbose_name='Idiomas en los que le interesa enviar o recibir información'),
        ),
        migrations.AddField(
            model_name='customeruser',
            name='mobile',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Número móvil o WhatsApp'),
        ),
        migrations.AddField(
            model_name='customeruser',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Déjenos un número de teléfono donde le podamos contactar'),
        ),
        migrations.AddField(
            model_name='customeruser',
            name='plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='landing_page.Plan', verbose_name='Plan'),
        ),
        migrations.AddField(
            model_name='customeruser',
            name='postal_code',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Código postal'),
        ),
        migrations.AddField(
            model_name='customeruser',
            name='state',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Ciudad / Estado / Parroquia'),
        ),
        migrations.AddField(
            model_name='customeruser',
            name='subscription_id',
            field=models.CharField(blank=True, editable=False, max_length=50, null=True, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
        migrations.AddField(
            model_name='customeruser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='customeruser',
            name='web_site',
            field=models.URLField(blank=True, null=True, verbose_name='Déjenos su dirección Web'),
        ),
        migrations.AlterField(
            model_name='customeruser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='customeruser',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='customeruser',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]