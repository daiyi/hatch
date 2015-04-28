# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '__first__'),
        ('incubator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incubator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('owner', models.OneToOneField(to='account.Account')),
            ],
        ),
    ]
