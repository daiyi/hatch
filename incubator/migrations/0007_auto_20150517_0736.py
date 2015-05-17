# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import incubator.models


class Migration(migrations.Migration):

    dependencies = [
        ('incubator', '0006_auto_20150517_0632'),
    ]

    operations = [
        migrations.RenameField(
            model_name='egg',
            old_name='name',
            new_name='nickname',
        ),
        migrations.AlterField(
            model_name='incubator',
            name='last_updated',
            field=models.PositiveIntegerField(default=incubator.models.epoch_time_now),
        ),
    ]
