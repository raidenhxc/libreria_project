# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0005_auto_20141001_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='estanteria',
            field=models.ForeignKey(to='libreria.Estanteria', on_delete=django.db.models.deletion.PROTECT),
        ),
    ]
