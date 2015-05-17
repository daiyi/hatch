# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('incubator', '0007_auto_20150517_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='egg',
            name='nickname',
            field=models.CharField(default=b'', max_length=12, blank=True),
        ),
    ]
