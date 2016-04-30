"""bolg06 URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from app06.views import add,art_list,topic,edit,index,search,art_comment
from django.contrib.auth.views import login,logout
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^add/$', add),
    url(r'^art_list_(?P<uid>\d+)_(?P<cid>\d+)/$', art_list),
    url(r'^topic_(?P<id>\d+)/$', topic),
    url(r'^edit_(?P<id>\d+)/$', edit),
    url(r'^search/$', search),
    url(r'^art_comment/$', art_comment),
    url(r'^accounts/login/$',login,{'template_name':'login.html'}),
    url(r'^accounts/logout/$',logout,{'template_name':'logout.html'})
]

if not settings.DEBUG:
    urlpatterns += url(r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT,})
