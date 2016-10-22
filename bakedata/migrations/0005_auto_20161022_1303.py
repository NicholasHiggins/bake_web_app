# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bakedata', '0004_auto_20161022_1221'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formula',
            old_name='ingredients_used',
            new_name='ingredients',
        ),
        migrations.RenameField(
            model_name='ingredient',
            old_name='stock_amount',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='ratio',
            old_name='percent',
            new_name='ratio',
        ),
    ]
