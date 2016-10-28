# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bakedata', '0006_load_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='load',
            name='name',
        ),
    ]
