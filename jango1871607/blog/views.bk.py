#coding:utf8
from django.shortcuts import render,render_to_response,HttpResponseRedirect,HttpResponse
from blog.models import article
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.
def index(req):
    return HttpResponse('index')

def add(req):
    if req.method == 'POST':
        action = req.GET.get('action')
        title = req.POST.get('title',None)
        content = req.POST.get('content',None)
        if action == 'add':
            a = article(title=title,content=content)
            a.save()
        elif action == 'edit':
            aid = req.GET.get('aid')
            article.objects.filter(id=aid).update(title=title,content=content)
        return HttpResponseRedirect('/art_list')
    else:
        action = req.GET.get('action',None)
        if action == 'add':
            return render(req,'add.html',{'action':action})
        elif action == 'edit':
            aid = req.GET.get('aid',None)
            art = article.objects.get(id=aid)
            return render(req,'add.html',{'art':art,'action':action})

def art_list(req):
    articles = article.objects.order_by('-pub_date').all()
    paginator = Paginator(articles,2)  # 第二个参数是 每页显示记录条数
    pn = req.GET.get('pn')
    try:
        articles = paginator.page(pn)
    except PageNotAnInteger: # 异常，页号非法
        articles = paginator.page(1)   # 显示第一页
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)  # 显示最后一页

    return render_to_response('art_list.html',{'articles':articles,'paginator':paginator})

def delete(req,id):
    return HttpResponse(id)