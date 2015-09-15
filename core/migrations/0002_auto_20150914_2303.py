# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crud',
            name='data',
            field=models.DateField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='crud',
            name='entrada',
            field=models.TimeField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='crud',
            name='saida',
            field=models.TimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
