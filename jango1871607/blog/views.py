# coding:utf8
from django.shortcuts import render, render_to_response, HttpResponseRedirect, HttpResponse
from blog.models import article,cat,comment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import connections
from qq.models import UserProfile,QQgroup

# Create your views here.
def index(req):
    users = User.objects.all()
    return render_to_response('index.html',{'users':users})

@login_required()
def add(req):
    if req.method == 'POST':
        title = req.POST.get('title', None)
        content = req.POST.get('content', None)
        cid = req.POST.get('cid',0)
        a = article(title=title, content=content)
        a.cats = cat(id=cid)
        a.user = User(id=req.user.id)
        a.save()
        return HttpResponseRedirect('/art_list/%s/0' % req.user.id)
    cats = cat.objects.filter(user_id=req.user.id).all()
    return render(req, 'add.html',{'cats':cats})

def art_list(req,uid,cid=0):
    wd = req.GET.get('wd','')
    if int(cid):
        articles = article.objects.filter(user_id=uid,cats_id=cid,title__contains=wd).order_by('-pub_date').all()   # 一个用户某个分类下的博客
    else:
        articles = article.objects.filter(user_id=uid,title__contains=wd).order_by('-pub_date').all()  # 一个用户所有博客
    paginator = Paginator(articles, 1)  # 第二个参数是 每页显示记录条数
    pn = req.GET.get('pn','1')
    # 设置页数
    if pn.isdigit():
        pn = int(pn)
        if pn > paginator.num_pages:
            pn = paginator.num_pages
        elif pn <= 0:
            pn = 1
    else:
        pn = 1
    try:
        articles = paginator.page(pn)
    except PageNotAnInteger:  # 异常，页号非法
        articles = paginator.page(1)  # 显示第一页
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)  # 显示最后一页
    page_range = paginator.page_range

    if pn > 2:
        page_range = page_range[pn - 2 - 1:pn + 2]
    else:
        if pn < 5:
            page_range = page_range[0:5]
        else:
            page_range = page_range[0:len(page_range)]
    suser = User.objects.get(id=uid)

    cats = suser.cats.all() # 用related_name 反向查询
    return render(req,'art_list.html', {'articles': articles, 'page_range': page_range,'cats':cats,'suser':suser,'wd':wd})

def edit(req,aid):
    if req.method == 'POST':
        title = req.POST.get('title', None)
        content = req.POST.get('content', None)
        cid = req.POST.get('cid',None)
        res = article.objects.filter(id=aid).update(title=title,content=content,cats_id=cid)
        return HttpResponseRedirect('/art_list/%s/0' % req.user.id)

    art = article.objects.get(id=aid)
    cats = cat.objects.filter(user_id=req.user.id).all()
    return render(req,'edit.html',{'art':art,'cats':cats})

def topic(req,aid):
    if req.method == 'POST':  # 文章评论
        comt = req.POST.get('comment','')
        c = comment(comt=comt)
        c.art = article(id=aid)
        c.save()
        return HttpResponseRedirect('/topic/%s' % aid)
    # 显示文章
    art = article.objects.get(id=aid)
    comments = art.comments.all() # 反向查询这个文章下的所有评论内容
    return render(req,'topic.html',{'art':art,'comments':comments})


def delete(req,aid):
    res = article.objects.filter(id=aid).delete()
    return HttpResponseRedirect('/art_list/%s/0' % req.user.id)

def register(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        email = req.POST.get('email')
        user = User.objects.create_user(username=username,password=password,email=email)
        user.save()
        # 添加关联
        userpro = UserProfile(name=username,user=User.objects.get(username=username))
        userpro.save()
        #进组
        beer = QQgroup.objects.get(name='原汁麦之夜')
        beer.member.add(userpro)
        # 添加默认分类
        uid = User.objects.get(username=username).id
        c = cat(name='其它',user_id=uid)
        c.save()

        return HttpResponseRedirect('/accounts/login/?next=/qq/')
    return render(req,'register.html')
