# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('incubator', '0002_incubator'),
    ]

    operations = [
        migrations.AddField(
            model_name='egg',
            name='incubator',
            field=models.ForeignKey(to='incubator.Incubator', null=True),
        ),
    ]
