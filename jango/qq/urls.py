#coding:utf8

from django.conf.urls import url,include
from views import index,dachui,dachui_redirect
urlpatterns = [
    url(r'^$', index,name='index'),
    url(r'^dachui/(\d+)/(\d+)/$', dachui_redirect),
    url(r'^xiaomei/(\d+)/(\d+)/$', dachui,name='dachui'),
]
