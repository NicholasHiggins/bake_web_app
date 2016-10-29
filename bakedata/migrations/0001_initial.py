# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bake',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('date_edited', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Formula',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('soaker_percent', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Load',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('loaf_mass', models.DecimalField(decimal_places=3, max_digits=6)),
                ('number_of_loaves', models.IntegerField()),
                ('formula', models.ForeignKey(to='bakedata.Formula')),
            ],
        ),
        migrations.CreateModel(
            name='Ratio',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('ratio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('formula', models.ForeignKey(to='bakedata.Formula')),
                ('ingredient', models.ForeignKey(to='bakedata.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='SoakerRatio',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('ratio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('formula', models.ForeignKey(to='bakedata.Formula')),
                ('ingredient', models.ForeignKey(to='bakedata.Ingredient')),
            ],
        ),
        migrations.AddField(
            model_name='formula',
            name='ingredients',
            field=models.ManyToManyField(related_name='Ratio', through='bakedata.Ratio', to='bakedata.Ingredient'),
        ),
        migrations.AddField(
            model_name='formula',
            name='soaker',
            field=models.ManyToManyField(related_name='SoakerRatio', through='bakedata.SoakerRatio', to='bakedata.Ingredient'),
        ),
        migrations.AddField(
            model_name='bake',
            name='loads',
            field=models.ManyToManyField(to='bakedata.Load'),
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
