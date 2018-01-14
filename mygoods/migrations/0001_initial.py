# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-01-14 08:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateField(auto_now_add=True, verbose_name='\u65e5\u671f')),
                ('kind', models.CharField(max_length=200, verbose_name='\u79cd\u7c7b')),
                ('goods_id', models.CharField(max_length=100, verbose_name='\u7f16\u53f7')),
                ('summary', models.TextField(verbose_name='\u6458\u8981')),
                ('get_in', models.IntegerField(default=0, verbose_name='\u6536\u5165\u6570\u91cf')),
                ('get_out', models.IntegerField(default=0, verbose_name='\u652f\u51fa\u6570\u91cf')),
                ('get_left', models.IntegerField(default=0, verbose_name='\u7ed3\u4f59\u6570\u91cf')),
            ],
            options={
                'ordering': ['-time'],
                'verbose_name': '\u5546\u54c1',
                'verbose_name_plural': '\u5546\u54c1',
            },
        ),
    ]