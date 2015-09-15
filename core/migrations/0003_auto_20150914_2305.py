# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150914_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crud',
            name='saida',
            field=models.TimeField(default=b'', null=True, blank=True),
            preserve_default=True,
        ),
    ]
