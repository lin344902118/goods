# -*- coding:utf-8 -*-

import datetime
import json
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import Goods


# Create your views here.
class AddView(View):
    def post(self, request):
        if not request.user.is_active:
            return redirect('/login')
        time = datetime.datetime.now()
        kind = request.POST.get('kind')
        goods_id = request.POST.get('goods_id')
        summary = request.POST.get('summary', '')
        get_in = int(request.POST.get('get_in'))
        get_out = int(request.POST.get('get_out'))
        get_left = get_in - get_out
        result = Goods.objects.create(time=time, kind=kind, goods_id=goods_id, summary=summary, get_in=get_in, get_out=get_out, get_left=get_left)
        if result:
            return redirect('/index')
        else:
            return render(request, 'show_goods.html', {'error': u'添加失败'})


class ModifyView(View):
    def post(self, request):
        if not request.user.is_active:
            return redirect('/login')
        time = datetime.datetime.now()
        id = request.POST.get('id')
        kind = request.POST.get('kind')
        goods_id = request.POST.get('goods_id')
        summary = request.POST.get('summary', '')
        get_in = int(request.POST.get('get_in'))
        get_out = int(request.POST.get('get_out'))
        get_left = get_in - get_out
        result = Goods.objects.filter(id=id).update(time=time, kind=kind, goods_id=goods_id, summary=summary, get_in=get_in, get_out=get_out, get_left=get_left)
        if result:
            return redirect('/index')
        else:
            return render(request, 'show_goods.html', {'error': u'修改失败'})


class DeleteView(View):
    def get(self, request):
        if not request.user.is_active:
            return redirect('/login')
        result = dict()
        try:
            id = request.GET.get('id')
            status = Goods.objects.filter(id=id).delete()
            if status[0]:
                result['ret'] = 0
                result['status'] = 'success'
            else:
                result['ret'] = 1
                result['status'] = 'failed'
        except Exception as e:
            result['ret'] = 10000
            result['status'] = 'failed'
            result['message'] = str(e)
        return HttpResponse(json.dumps(result), content_type="application/json")


class SearchView(View):
    def post(self, request):
        type = request.POST.get('type')
        search = request.POST.get('search')
        if not search:
            goods = Goods.objects.all()
        else:
            if type == 'time':
                search = datetime.datetime.strptime(search, '%Y-%m-%d')
                goods = Goods.objects.filter(time__gte=search.date())
            elif type == 'kind':
                goods = Goods.objects.filter(kind__contains=search)
            elif type == 'goods_id':
                goods = Goods.objects.filter(goods_id=search)
            else:
                goods = Goods.objects.filter(summary__contains=search)
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        except EmptyPage:
            page = 1
        p = Paginator(goods, per_page=20, request=request)
        goods = p.page(page)
        return render(request, 'show_goods.html', {'goods': goods})



