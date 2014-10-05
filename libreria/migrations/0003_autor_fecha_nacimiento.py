# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0002_remove_autor_fecha_nacimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.date(2014, 9, 29)),
            preserve_default=False,
        ),
    ]
