# coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Goods(models.Model):
    time = models.DateTimeField(auto_now_add=True, verbose_name=u'日期')
    kind = models.CharField(max_length=200, verbose_name=u'种类')
    goods_id = models.CharField(max_length=100, verbose_name=u'编号')
    image = models.ImageField(upload_to='goods', verbose_name=u'图片')
    summary = models.TextField(verbose_name=u'摘要')
    get_in = models.IntegerField(default=0, verbose_name=u'收入数量')
    get_out = models.IntegerField(default=0, verbose_name=u'支出数量')
    get_left = models.IntegerField(default=0, verbose_name=u'结余数量')
    state = models.IntegerField(default=0, verbose_name=u'状态')

    def __str__(self):
        return self.kind + self.goods_id

    class Meta:
        verbose_name = u'商品'
        verbose_name_plural = verbose_name
        ordering = ['-time']
