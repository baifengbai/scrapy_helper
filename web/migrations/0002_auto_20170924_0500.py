# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 05:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image_urls',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='images',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='md5',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='rule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Rule'),
        ),
        migrations.AlterField(
            model_name='project',
            name='domain',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='pipelines',
            field=models.CharField(choices=[(1, 'JsonWriterPipeline'), (2, 'ImagesPipeline')], max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[(0, '\u6784\u5efa\u4e2d'), (1, '\u521d\u59cb\u5316'), (2, '\u8fd0\u884c'), (3, '\u505c\u6b62')], default=0, max_length=1),
        ),
        migrations.AlterField(
            model_name='rule',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Project'),
        ),
    ]
