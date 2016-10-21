# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bakedata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formula',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Ratio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('ratio', models.DecimalField(max_digits=5, decimal_places=2)),
                ('formula', models.ForeignKey(to='bakedata.Formula')),
            ],
        ),
        migrations.RenameField(
            model_name='ingredient',
            old_name='amount',
            new_name='stock_amount',
        ),
        migrations.AddField(
            model_name='ratio',
            name='ingredient',
            field=models.ForeignKey(to='bakedata.Ingredient'),
        ),
        migrations.AddField(
            model_name='formula',
            name='ingredients',
            field=models.ManyToManyField(through='bakedata.Ratio', to='bakedata.Ingredient'),
        ),
    ]
