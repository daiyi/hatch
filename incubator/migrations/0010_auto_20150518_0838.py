# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('incubator', '0009_auto_20150517_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='egg',
            name='next_identity',
            field=models.CharField(default=b'kanto', max_length=12, blank=True),
        ),
    ]
