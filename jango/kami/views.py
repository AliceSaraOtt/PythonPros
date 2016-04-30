#coding:utf8
from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect,get_object_or_404
from django.template import Template,Context,loader  # 一种传统加载模板 渲染模板的方法，推荐用render_to_response
from kami.models import student

# Create your views here.

def index(request):
    s = student.objects.get('name=tina')
    return HttpResponse(1)

#url 参数传递测试
def param(request,i):
    return HttpResponse(i)

class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def say(self):
        return 'Hello 我是say方法'
def test(request):
    user = {'name':'大锤','age':16} # 字典分配数据 用法见模板
    book = ['python','php','matplotlib'] # 列表分配数据
    person = Human('大锤',16)
    #三种数据结构传递给模板访问时的优先级（字典，对象属性，对象方法，列表）
    return render_to_response('test.html',{'user':user,'book':book,'person':person})