# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bakedata', '0003_auto_20161022_1219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ratio',
            old_name='ratio',
            new_name='percent',
        ),
    ]
