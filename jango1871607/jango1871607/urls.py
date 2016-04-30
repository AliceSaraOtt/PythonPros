"""jango1871607 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from blog.views import index,add,art_list,edit,delete,register,topic
from django.contrib.auth.views import login,logout
from qq import urls as qq_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='index'),
    url(r'^add/$', add, name='add'),
    url(r'^edit/(?P<aid>\d+)/$', edit, name='edit'),
    url(r'^delete/(?P<aid>\d+)/$', delete, name='delete'),
    url(r'^art_list/(?P<uid>\d+)/(?P<cid>\d+)/$', art_list, name='art_list'),
    url(r'^topic/(?P<aid>\d+)/$',topic, name='topic'),
    url(r'^accounts/login/$', login, {'template_name':'login.html'},name='login'),
    url(r'^accounts/logout/$', logout, {'template_name':'logout.html'},name='logout'),
    url(r'^register/$', register, name='register'),
    url(r'^qq/', include(qq_urls)),
]