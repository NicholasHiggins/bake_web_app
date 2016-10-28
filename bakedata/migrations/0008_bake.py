# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bakedata', '0007_remove_load_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bake',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('date_edited', models.DateField(auto_now=True)),
                ('loads', models.ManyToManyField(to='bakedata.Load')),
            ],
        ),
    ]
