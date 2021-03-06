# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 05:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emeros', '0003_auto_20171109_2158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='palazzo',
            name='fit_type',
        ),
        migrations.RemoveField(
            model_name='palazzo',
            name='size_p',
        ),
        migrations.AddField(
            model_name='palazzo',
            name='color',
            field=models.CharField(blank=True, default='default', max_length=50),
        ),
        migrations.AddField(
            model_name='palazzo',
            name='country',
            field=models.CharField(default='India', max_length=10),
        ),
        migrations.AddField(
            model_name='palazzo',
            name='description',
            field=models.TextField(default='Write here'),
        ),
        migrations.AddField(
            model_name='palazzo',
            name='ideal_for',
            field=models.CharField(default='female', max_length=10),
        ),
        migrations.AddField(
            model_name='palazzo',
            name='item_name',
            field=models.CharField(default='Palazzo', max_length=200),
        ),
        migrations.AddField(
            model_name='palazzo',
            name='key_feature1',
            field=models.CharField(default='write here', max_length=50),
        ),
        migrations.AddField(
            model_name='palazzo',
            name='key_feature2',
            field=models.CharField(default='write here', max_length=50),
        ),
        migrations.AddField(
            model_name='palazzo',
            name='key_feature3',
            field=models.CharField(default='write here', max_length=50),
        ),
        migrations.AddField(
            model_name='palazzo',
            name='key_feature4',
            field=models.CharField(default='write here', max_length=50),
        ),
        migrations.AddField(
            model_name='palazzo',
            name='key_feature5',
            field=models.CharField(default='write here', max_length=50),
        ),
        migrations.AddField(
            model_name='palazzo',
            name='keywords',
            field=models.CharField(default='write here', max_length=200),
        ),
        migrations.AddField(
            model_name='palazzo',
            name='material',
            field=models.CharField(choices=[('Crepe', 'Crepe'), ('Cotton', 'Cotton')], default='Crepe', max_length=15),
        ),
        migrations.AddField(
            model_name='palazzo',
            name='mrp',
            field=models.IntegerField(default=899),
        ),
        migrations.AddField(
            model_name='palazzo',
            name='num_items',
            field=models.IntegerField(blank=True, default='1'),
        ),
        migrations.AddField(
            model_name='palazzo',
            name='occasion',
            field=models.CharField(default='Casual', max_length=50),
        ),
        migrations.AddField(
            model_name='palazzo',
            name='pack_height',
            field=models.PositiveIntegerField(blank=True, default='5'),
        ),
        migrations.AddField(
            model_name='palazzo',
            name='pack_length',
            field=models.PositiveIntegerField(blank=True, default='20'),
        ),
        migrations.AddField(
            model_name='palazzo',
            name='pack_width',
            field=models.PositiveIntegerField(blank=True, default='20'),
        ),
        migrations.AddField(
            model_name='palazzo',
            name='package_num',
            field=models.IntegerField(blank=True, default='1'),
        ),
        migrations.AddField(
            model_name='palazzo',
            name='package_weight',
            field=models.FloatField(blank=True, default='0.25'),
        ),
        migrations.AddField(
            model_name='palazzo',
            name='qty',
            field=models.PositiveIntegerField(blank=True, default='5'),
        ),
        migrations.AddField(
            model_name='palazzo',
            name='size',
            field=models.CharField(choices=[('M', 'M'), ('XL', 'XL'), ('XXL', 'XXL')], default='M', max_length=10),
        ),
        migrations.AddField(
            model_name='palazzo',
            name='sp',
            field=models.IntegerField(default=899),
        ),
        migrations.AddField(
            model_name='palazzo',
            name='upc',
            field=models.BigIntegerField(blank=True, default='0123456789'),
        ),
        migrations.AlterField(
            model_name='palazzo',
            name='brand',
            field=models.CharField(default='Emeros', max_length=10),
        ),
        migrations.DeleteModel(
            name='Apparel',
        ),
    ]
