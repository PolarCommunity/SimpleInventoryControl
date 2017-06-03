# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-03 03:50
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleIngreso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=15)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.Articulo')),
            ],
        ),
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('descripcion', models.CharField(max_length=150)),
                ('comprobante', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='detalleingreso',
            name='ingreso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingresos.Ingreso'),
        ),
    ]