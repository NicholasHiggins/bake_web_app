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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Load',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('loaf_mass', models.DecimalField(decimal_places=3, max_digits=6)),
                ('number_of_loaves', models.IntegerField()),
                ('formula', models.ForeignKey(to='bakedata.Formula')),
            ],
        ),
        migrations.CreateModel(
            name='Ratio',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('ratio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('formula', models.ForeignKey(to='bakedata.Formula')),
                ('ingredient', models.ForeignKey(to='bakedata.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='SoakerRatio',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('ratio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('formula', models.ForeignKey(to='bakedata.Formula')),
                ('ingredient', models.ForeignKey(to='bakedata.Ingredient')),
            ],
        ),
        migrations.AddField(
            model_name='formula',
            name='ingredients',
            field=models.ManyToManyField(to='bakedata.Ingredient', related_name='Ratio', through='bakedata.Ratio'),
        ),
        migrations.AddField(
            model_name='formula',
            name='soaker',
            field=models.ManyToManyField(to='bakedata.Ingredient', related_name='SoakerRatio', through='bakedata.SoakerRatio'),
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
