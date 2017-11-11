# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-09 16:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emeros', '0002_auto_20171109_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apparel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(default='Emeros', max_length=6)),
                ('size', models.CharField(choices=[('28', 'M'), ('34', 'XL'), ('40', 'XXL')], max_length=5, unique=True)),
                ('size_unit', models.CharField(blank=True, max_length=5)),
                ('regular_fit', models.CharField(blank=True, default='Regular Fit', max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Palazzo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.SlugField()),
                ('brand', models.CharField(default='Emeros', max_length=12)),
                ('fit_type', models.CharField(blank=True, default='Regular Fit', max_length=12)),
                ('size_p', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emeros.Apparel', to_field='size')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]