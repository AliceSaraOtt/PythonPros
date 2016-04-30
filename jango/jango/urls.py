#coding:utf8
"""jango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from kami.views import index,param,test
from kami import views
from qq import urls as qq_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^test/$', test),
    url(r'^qq/', include(qq_urls)),
    #url(r'^(?P<id>[\d]+)$', index), # 给views里的函数传参，如果给正则分组起别名，则参数名就是id
    #url(r'^param/(\d+)$', param), # 不起名则默认安顺序传参
]
