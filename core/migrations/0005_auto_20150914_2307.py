# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150914_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crud',
            name='saida',
            field=models.TimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
