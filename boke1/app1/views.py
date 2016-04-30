#coding:utf8
from django.shortcuts import render,render_to_response,HttpResponseRedirect,HttpResponse
from app1.models import article,comment,cat
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
# Create your views here.

#添加博客
@login_required
def add(request):
    user = request.user
    c = csrf(request)
    if request.method == 'POST':
        title = request.POST.get('title',None)
        content = request.POST.get('content',None)
        cat_id = request.POST.get('cat_id',None)
        if title and content:
            b = article(title=title,content=content,cat_id=cat_id)
            b.user = User(id=user.id)
            b.save()
            return HttpResponseRedirect('/list_%s_%s' % (user.id, cat_id))
        else:
            return render_to_response('error.html',{'e':'标题或内容不能为空'})
    #处理添加显示模板
    cats = cat.objects.filter(user_id=user.id).all()
    return render_to_response('add.html',{'c':c,'cats':cats})

def list(request,uid=None,cid=None):
    user = request.user # 发起请求的用户
    if uid and cid:
        contacts = article.objects.filter(user_id=uid,cat_id=cid).order_by('-id').all()
    elif uid:
        contacts = article.objects.filter(user_id=uid).order_by('-id').all()
    else:
        contacts = article.objects.order_by('-id').all()
    paginator = Paginator(contacts, 5)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    page_range = paginator.page_range # 分页数字
    # 获取username
    suser = User.objects.get(id=uid) # 显示的用户
    showe = 0 # 是否显示编辑
    if uid and user.id:
        if int(uid) == int(user.id):
            showe = 1
    # 获取分类信息
    #cats = cat.objects.filter(user_id=uid).all() # 普通方法
    cats = suser.cat.all()  # 用suser 的related_name 反向引用
    return render_to_response('list.html',{'contacts': contacts,'page_range':page_range,'suser':suser,'showe':showe,'cats':cats})

#内容页
def topic(request,id):
    c = csrf(request)
    art = article.objects.get(id=id)
    #comments = comment.objects.filter(art=id).order_by('-id').all()
    comments = art.comments.order_by('-id').all() # 用过related_name 反向用一调用多条记录方法
    return render_to_response('topic.html',{'article':art,'comments':comments,'c':c})

#添加评论
@login_required
def art_comment(request):
    if request.method == 'POST':
        content = request.POST.get('content',None)
        art_id = request.POST.get('art_id', None)
        c = comment()
        c.content = content
        c.art = article(id=art_id)
        c.save()
        return HttpResponseRedirect('/topic_%s' % art_id)

# 编辑
def edit(request,id):
    user = request.user
    c = csrf(request)
    if request.method == 'POST':
        title = request.POST.get('title',None)
        content = request.POST.get('content',None)
        cat_id = request.POST.get('cat_id',None)
        if title and content:
            b = article(id=id,user_id=user.id)
            b.title = title
            b.content = content
            b.cat_id = cat_id
            b.save()
            return HttpResponseRedirect('/list_%s_%s' % (user.id,cat_id) )
        else:
            return render_to_response('error.html',{'e':'标题或内容不能为空'})
    #处理添加显示模板
    art = article.objects.get(id=id) # 拿到一个博客内容
    cats = cat.objects.filter(user_id=user.id).all()
    return render_to_response('edit.html',{'c':c,'cats':cats,'art':art})

def search(request):
    keyword = request.GET.get('keyword',None)
    articles = article.objects.filter(title__contains=keyword).all()
    return render_to_response('list.html',{'contacts':articles,'keyword':keyword})

def index(request):
    # if request.user.is_authenticated():     #判断用户是否已登录
    #     user = request.user
    # else:
    #     user = request.user # 匿名用户
    # return HttpResponse(user.email)
    return render_to_response('index.html')