# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('incubator', '0004_auto_20150504_0327'),
    ]

    operations = [
        migrations.AddField(
            model_name='egg',
            name='focus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='incubator',
            name='last_updated',
            field=models.PositiveIntegerField(default=1431754770),
        ),
    ]
