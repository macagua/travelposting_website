# Generated by Django 2.1.12 on 2019-09-30 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0007_auto_20190927_1646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='categorie',
        ),
        migrations.AddField(
            model_name='destination',
            name='categorie',
            field=models.ManyToManyField(blank=True, null=True, to='destinations.Categorie', verbose_name='Categorie'),
        ),
        migrations.AlterField(
            model_name='destination',
            name='description',
            field=models.TextField(blank=True, default='\n<strong>Ingrese su título aquí...</strong><br><br>\n\n<p> <b>Ingrese aquí su texto...</b></p>\n\n<!--more--><br><br>\n\n<p> <b>Ingrese más información aquí...</b></p>\n\n<!--more--><br><br>\n\n<strong>Quienes somos</strong><br><br>\n\n<p><b>Por favor ingrese aquí su texto...</b></p><br><br>\n\n<strong>Misión</strong><br><br>\n\n<p><b>Por favor ingrese aquí su texto...</b></p><br><br>\n\n<table class="table table-bordered tours-tabs__table" style="width: 100%px;">\n<tbody>\n<tr>\n <td style="width: 213px;"><strong>SALIDA / RETORNO</strong></td>\n <td style="width: 574.233px;"><b>Ingrese aquí la salida...</b></td>\n</tr>\n<tr>\n <td style="width: 213px;"><strong>HORA DE SALIDA</strong></td>\n <td style="width: 574.233px;"><b>Ingrese aquí la hora de salida...</b></td>\n</tr>\n<tr>\n <td style="width: 213px;"><strong>HORA DE LLEGADA</strong></td>\n <td style="width: 574.233px;"><b>Ingrese aquí la hora de llegada...</b></td>\n</tr>\n<tr>\n <td style="width: 213px;"><strong>NR. DE TOUR PARA RESERVAS</strong></td>\n <td style="width: 574.233px;"><b>Ingrese aquí el nro de tour...</b></td>\n</tr>\n<tr>\n <td style="width: 213px;"><strong>TRASLADO DESDE </strong></td>\n <td style="width: 574.233px;"><strong><b>Ingrese aquí el traslado...</b></strong></td>\n</tr>\n<tr>\n <td style="width: 213px;"><strong>INCLUIDO</strong></td>\n <td style="width: 574.233px;">\n  <b>Ingrese aquí lo que va incluido en el paquete como una lista...</b>\n  <ul><li><b><br></b></li><li><b><br></b></li><li><b><br></b></li></ul>\n </td>\n</tr>\n<tr>\n <td style="width: 213px;"><strong>NO INCLUIDO</strong></td>\n <td style="width: 574.233px;">\n  <b>Ingrese aquí lo que no va incluido en el paquete como una lista...</b>\n  <ul><li><b><br></b></li><li><b><br></b></li><li><b><br></b></li></ul>\n </td>\n</tr>\n</tbody>\n</table>\n', null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='destination',
            name='description_de',
            field=models.TextField(blank=True, default='\n<strong>Ingrese su título aquí...</strong><br><br>\n\n<p> <b>Ingrese aquí su texto...</b></p>\n\n<!--more--><br><br>\n\n<p> <b>Ingrese más información aquí...</b></p>\n\n<!--more--><br><br>\n\n<strong>Quienes somos</strong><br><br>\n\n<p><b>Por favor ingrese aquí su texto...</b></p><br><br>\n\n<strong>Misión</strong><br><br>\n\n<p><b>Por favor ingrese aquí su texto...</b></p><br><br>\n\n<table class="table table-bordered tours-tabs__table" style="width: 100%px;">\n<tbody>\n<tr>\n <td style="width: 213px;"><strong>SALIDA / RETORNO</strong></td>\n <td style="width: 574.233px;"><b>Ingrese aquí la salida...</b></td>\n</tr>\n<tr>\n <td style="width: 213px;"><strong>HORA DE SALIDA</strong></td>\n <td style="width: 574.233px;"><b>Ingrese aquí la hora de salida...</b></td>\n</tr>\n<tr>\n <td style="width: 213px;"><strong>HORA DE LLEGADA</strong></td>\n <td style="width: 574.233px;"><b>Ingrese aquí la hora de llegada...</b></td>\n</tr>\n<tr>\n <td style="width: 213px;"><strong>NR. DE TOUR PARA RESERVAS</strong></td>\n <td style="width: 574.233px;"><b>Ingrese aquí el nro de tour...</b></td>\n</tr>\n<tr>\n <td style="width: 213px;"><strong>TRASLADO DESDE </strong></td>\n <td style="width: 574.233px;"><strong><b>Ingrese aquí el traslado...</b></strong></td>\n</tr>\n<tr>\n <td style="width: 213px;"><strong>INCLUIDO</strong></td>\n <td style="width: 574.233px;">\n  <b>Ingrese aquí lo que va incluido en el paquete como una lista...</b>\n  <ul><li><b><br></b></li><li><b><br></b></li><li><b><br></b></li></ul>\n </td>\n</tr>\n<tr>\n <td style="width: 213px;"><strong>NO INCLUIDO</strong></td>\n <td style="width: 574.233px;">\n  <b>Ingrese aquí lo que no va incluido en el paquete como una lista...</b>\n  <ul><li><b><br></b></li><li><b><br></b></li><li><b><br></b></li></ul>\n </td>\n</tr>\n</tbody>\n</table>\n', null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='destination',
            name='description_en',
            field=models.TextField(blank=True, default='\n<strong>Ingrese su título aquí...</strong><br><br>\n\n<p> <b>Ingrese aquí su texto...</b></p>\n\n<!--more--><br><br>\n\n<p> <b>Ingrese más información aquí...</b></p>\n\n<!--more--><br><br>\n\n<strong>Quienes somos</strong><br><br>\n\n<p><b>Por favor ingrese aquí su texto...</b></p><br><br>\n\n<strong>Misión</strong><br><br>\n\n<p><b>Por favor ingrese aquí su texto...</b></p><br><br>\n\n<table class="table table-bordered tours-tabs__table" style="width: 100%px;">\n<tbody>\n<tr>\n <td style="width: 213px;"><strong>SALIDA / RETORNO</strong></td>\n <td style="width: 574.233px;"><b>Ingrese aquí la salida...</b></td>\n</tr>\n<tr>\n <td style="width: 213px;"><strong>HORA DE SALIDA</strong></td>\n <td style="width: 574.233px;"><b>Ingrese aquí la hora de salida...</b></td>\n</tr>\n<tr>\n <td style="width: 213px;"><strong>HORA DE LLEGADA</strong></td>\n <td style="width: 574.233px;"><b>Ingrese aquí la hora de llegada...</b></td>\n</tr>\n<tr>\n <td style="width: 213px;"><strong>NR. DE TOUR PARA RESERVAS</strong></td>\n <td style="width: 574.233px;"><b>Ingrese aquí el nro de tour...</b></td>\n</tr>\n<tr>\n <td style="width: 213px;"><strong>TRASLADO DESDE </strong></td>\n <td style="width: 574.233px;"><strong><b>Ingrese aquí el traslado...</b></strong></td>\n</tr>\n<tr>\n <td style="width: 213px;"><strong>INCLUIDO</strong></td>\n <td style="width: 574.233px;">\n  <b>Ingrese aquí lo que va incluido en el paquete como una lista...</b>\n  <ul><li><b><br></b></li><li><b><br></b></li><li><b><br></b></li></ul>\n </td>\n</tr>\n<tr>\n <td style="width: 213px;"><strong>NO INCLUIDO</strong></td>\n <td style="width: 574.233px;">\n  <b>Ingrese aquí lo que no va incluido en el paquete como una lista...</b>\n  <ul><li><b><br></b></li><li><b><br></b></li><li><b><br></b></li></ul>\n </td>\n</tr>\n</tbody>\n</table>\n', null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='destination',
            name='description_es',
            field=models.TextField(blank=True, default='\n<strong>Ingrese su título aquí...</strong><br><br>\n\n<p> <b>Ingrese aquí su texto...</b></p>\n\n<!--more--><br><br>\n\n<p> <b>Ingrese más información aquí...</b></p>\n\n<!--more--><br><br>\n\n<strong>Quienes somos</strong><br><br>\n\n<p><b>Por favor ingrese aquí su texto...</b></p><br><br>\n\n<strong>Misión</strong><br><br>\n\n<p><b>Por favor ingrese aquí su texto...</b></p><br><br>\n\n<table class="table table-bordered tours-tabs__table" style="width: 100%px;">\n<tbody>\n<tr>\n <td style="width: 213px;"><strong>SALIDA / RETORNO</strong></td>\n <td style="width: 574.233px;"><b>Ingrese aquí la salida...</b></td>\n</tr>\n<tr>\n <td style="width: 213px;"><strong>HORA DE SALIDA</strong></td>\n <td style="width: 574.233px;"><b>Ingrese aquí la hora de salida...</b></td>\n</tr>\n<tr>\n <td style="width: 213px;"><strong>HORA DE LLEGADA</strong></td>\n <td style="width: 574.233px;"><b>Ingrese aquí la hora de llegada...</b></td>\n</tr>\n<tr>\n <td style="width: 213px;"><strong>NR. DE TOUR PARA RESERVAS</strong></td>\n <td style="width: 574.233px;"><b>Ingrese aquí el nro de tour...</b></td>\n</tr>\n<tr>\n <td style="width: 213px;"><strong>TRASLADO DESDE </strong></td>\n <td style="width: 574.233px;"><strong><b>Ingrese aquí el traslado...</b></strong></td>\n</tr>\n<tr>\n <td style="width: 213px;"><strong>INCLUIDO</strong></td>\n <td style="width: 574.233px;">\n  <b>Ingrese aquí lo que va incluido en el paquete como una lista...</b>\n  <ul><li><b><br></b></li><li><b><br></b></li><li><b><br></b></li></ul>\n </td>\n</tr>\n<tr>\n <td style="width: 213px;"><strong>NO INCLUIDO</strong></td>\n <td style="width: 574.233px;">\n  <b>Ingrese aquí lo que no va incluido en el paquete como una lista...</b>\n  <ul><li><b><br></b></li><li><b><br></b></li><li><b><br></b></li></ul>\n </td>\n</tr>\n</tbody>\n</table>\n', null=True, verbose_name='description'),
        ),
    ]