# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bakedata', '0002_formula_soaker_percent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formula',
            name='soaker_percent',
            field=models.IntegerField(default=0),
        ),
    ]
