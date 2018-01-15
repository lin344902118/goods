# -*- coding:utf-8 -*-

from django.conf.urls import url
from .views import AddView, ModifyView,  DeleteView

urlpatterns = [
    url(r'^add', AddView.as_view(), name='add'),
    url(r'^modify', ModifyView.as_view(), name='modify'),
    url(r'^delete', DeleteView.as_view(), name='delete'),
]