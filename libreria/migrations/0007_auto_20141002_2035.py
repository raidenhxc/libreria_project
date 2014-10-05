# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0006_auto_20141001_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='autor',
            field=models.ForeignKey(to='libreria.Autor', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AlterField(
            model_name='libro',
            name='genero',
            field=models.ForeignKey(to='libreria.Genero', on_delete=django.db.models.deletion.PROTECT),
        ),
    ]
