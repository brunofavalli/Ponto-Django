# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crud',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
                ('data', models.DateField(auto_now_add=True)),
                ('entrada', models.TimeField(auto_now_add=True)),
                ('saida', models.TimeField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
