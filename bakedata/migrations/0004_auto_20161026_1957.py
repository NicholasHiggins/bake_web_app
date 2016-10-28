# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bakedata', '0003_auto_20161026_1510'),
    ]

    operations = [
        migrations.CreateModel(
            name='Load',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('loaf_mass', models.DecimalField(max_digits=6, decimal_places=3)),
                ('number_of_loaves', models.IntegerField()),
                ('formula', models.ForeignKey(to='bakedata.Formula')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('ingredient', models.ForeignKey(to='bakedata.Ingredient')),
                ('load', models.ForeignKey(to='bakedata.Load')),
            ],
        ),
        migrations.AddField(
            model_name='load',
            name='ingredients',
            field=models.ManyToManyField(through='bakedata.Recipe', to='bakedata.Ingredient', related_name='Recipe'),
        ),
    ]
