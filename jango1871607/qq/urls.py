from django.conf.urls import url
from views import home,sendMsg,getMsg,test
urlpatterns = [
    url(r'^$', home),
    url(r'^sendMsg/$', sendMsg,name='sendMsg'),
    url(r'^getMsg/$', getMsg,name='getMsg'),
    url(r'^test/$', test,name='test'),
]