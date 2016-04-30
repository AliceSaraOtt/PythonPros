from django.conf.urls import url
from views import home,sendMsg,getMsg
#from app1.views import topic
urlpatterns = [
    url(r'^$',home),
    url(r'^sendMsg/$',sendMsg,name='sendMsg'),
    url(r'^getMsg/$',getMsg,name='getMsg'),
]