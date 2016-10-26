# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formula',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('amount', models.DecimalField(max_digits=6, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Ratio',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('ratio', models.DecimalField(max_digits=5, decimal_places=2)),
                ('formula', models.ForeignKey(to='bakedata.Formula')),
                ('ingredient', models.ForeignKey(to='bakedata.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='SoakerRatio',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('ratio', models.DecimalField(max_digits=5, decimal_places=2)),
                ('formula', models.ForeignKey(to='bakedata.Formula')),
                ('ingredient', models.ForeignKey(to='bakedata.Ingredient')),
            ],
        ),
        migrations.AddField(
            model_name='formula',
            name='ingredients',
            field=models.ManyToManyField(through='bakedata.Ratio', to='bakedata.Ingredient', related_name='Ratio'),
        ),
        migrations.AddField(
            model_name='formula',
            name='soaker',
            field=models.ManyToManyField(through='bakedata.SoakerRatio', to='bakedata.Ingredient', related_name='SoakerRatio'),
        ),
        migrations.AlterUniqueTogether(
            name='soakerratio',
            unique_together=set([('ingredient', 'formula')]),
        ),
        migrations.AlterUniqueTogether(
            name='ratio',
            unique_together=set([('ingredient', 'formula')]),
        ),
    ]
