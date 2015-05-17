# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('incubator', '0005_auto_20150516_0539'),
    ]

    operations = [
        migrations.AddField(
            model_name='egg',
            name='identity',
            field=models.CharField(default=b'random', max_length=12),
        ),
        migrations.AddField(
            model_name='egg',
            name='name',
            field=models.CharField(default=b'', max_length=12),
        ),
        migrations.AlterField(
            model_name='incubator',
            name='last_updated',
            field=models.PositiveIntegerField(default=1431844333),
        ),
    ]
