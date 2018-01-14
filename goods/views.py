# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth import logout, login, authenticate
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from mygoods.models import Goods

# Create your views here.
class IndexView(View):
    def get(self, request):
        if not request.user.is_active:
            return redirect('/login')
        goods = Goods.objects.all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        except EmptyPage:
            page = 1
        p = Paginator(goods, per_page=20, request=request)
        goods = p.page(page)
        return render(request, 'show_goods.html', {'goods': goods})


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/index')
        return render(request, 'login.html', {'error': u'用户名或者密码错误'})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return (redirect('/login'))