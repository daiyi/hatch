# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('incubator', '0003_egg_incubator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incubator',
            name='owner',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
