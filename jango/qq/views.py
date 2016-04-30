#coding:utf8
from django.shortcuts import render,HttpResponse,render_to_response,HttpResponseRedirect
from django.core.urlresolvers import reverse
import random as r

# Create your views here.
def index(request):
    print request.GET
    nums = map(str,range(10))
    QQ = []
    score = r.randint(0,100)
    return render_to_response('index.html',{'get':request.GET,'nums':nums,'score':score})

def dachui(request,p1,p2):
    return HttpResponse('lalala')
    # return HttpResponseRedirect(reverse('add2', args=(p1, p2)))

def dachui_redirect(request,p1,p2):
    return HttpResponseRedirect(reverse('dachui', args=(p1, p2)))
    # return HttpResponseRedirect('/qq/xiaomei/%s/%s/' % (p1,p2)) # 不推荐