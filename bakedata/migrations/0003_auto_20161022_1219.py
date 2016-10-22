# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bakedata', '0002_auto_20161021_2018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formula',
            old_name='ingredients',
            new_name='ingredients_used',
        ),
    ]
