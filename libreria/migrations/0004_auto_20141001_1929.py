# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0003_autor_fecha_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genero',
            name='nombre',
            field=models.CharField(unique=True, max_length=128),
        ),
        migrations.AlterUniqueTogether(
            name='autor',
            unique_together=set([('apellidos', 'nombre')]),
        ),
    ]
