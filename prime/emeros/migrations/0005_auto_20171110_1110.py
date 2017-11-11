# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 05:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emeros', '0004_auto_20171110_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='palazzo',
            name='img1',
            field=models.ImageField(default='add image', upload_to=b''),
        ),
        migrations.AlterField(
            model_name='palazzo',
            name='size',
            field=models.CharField(choices=[('M', 'M'), ('XL', 'XL'), ('XXL', 'XXL')], default='XL', max_length=10),
        ),
    ]