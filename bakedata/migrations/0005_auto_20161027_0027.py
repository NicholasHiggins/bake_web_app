# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bakedata', '0004_auto_20161026_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingredient',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='load',
        ),
        migrations.RemoveField(
            model_name='load',
            name='ingredients',
        ),
        migrations.DeleteModel(
            name='Recipe',
        ),
    ]
