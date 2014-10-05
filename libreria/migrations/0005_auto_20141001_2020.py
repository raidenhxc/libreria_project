# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0004_auto_20141001_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='fecha_publicacion',
            field=models.DateField(default=datetime.date(2014, 10, 1)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='estanteria',
            name='nombre',
            field=models.CharField(unique=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='libro',
            name='nombre',
            field=models.CharField(unique=True, max_length=128),
        ),
    ]
