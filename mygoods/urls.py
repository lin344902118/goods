# -*- coding:utf-8 -*-

from django.conf.urls import url
from .views import AddView, ModifyView, DeleteView, SearchView

urlpatterns = [
    url(r'^add', AddView.as_view(), name='add'),
    url(r'^modify', ModifyView.as_view(), name='modify'),
    url(r'^delete', DeleteView.as_view(), name='delete'),
    url(r'^search', SearchView.as_view(), name='search'),
]