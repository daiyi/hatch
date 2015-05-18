# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('incubator', '0008_auto_20150517_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='egg',
            name='next_identity',
            field=models.CharField(default=b'kanto', max_length=12),
        ),
        migrations.AlterField(
            model_name='egg',
            name='identity',
            field=models.CharField(default=b'egg', max_length=12),
        ),
    ]
