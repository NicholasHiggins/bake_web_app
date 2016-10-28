# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bakedata', '0005_auto_20161027_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='load',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
