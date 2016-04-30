#coding:utf8
from django.shortcuts import render,render_to_response,HttpResponseRedirect,HttpResponse
from app06.models import Article,cat,comment
from django.core.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def magicNum(pn, page_range, max_num):
    half = max_num / 2
    if pn > half:
        page_range = list(page_range)[pn - half - 1:pn + half]
    else:
        if len(page_range) >= max_num:
            page_range = list(page_range)[0:max_num]
        else:
            page_range = list(page_range)[0:len(page_range)]
    return page_range

@login_required()
def add(request):
    user = request.user
    c = csrf(request)
    if request.method == 'POST': # 提交添加请求
        title = request.POST.get('title',None)
        content = request.POST.get('content',None)
        cat_id = request.POST.get('cat_id',None)
        if title and content:
            art = Article(title=title,content=content,cat_id=cat_id)
            art.user = User(id=user.id)
            art.save()
            return HttpResponseRedirect('/art_list_%s_%s/' % (user.id,cat_id)) # 添加成功跳转列表页
        else:
            return render_to_response('error.html',{'e':'标题或者内容不能为空'}) # 添加错误 到错误页面
    # 添加请求
    cats = cat.objects.filter(user_id=user.id).all()
    return render_to_response('add.html',{'c':c,'cats':cats})

def art_list(request,uid,cid=None):
    user = request.user # 发起请求的用户
    if int(cid):
        articles = Article.objects.filter(user_id=uid,cat_id=cid).order_by('-id').all() # 所有记录条数
    else:
        articles = Article.objects.filter(user_id=uid).order_by('-id').all() # 所有记录条数

    paginator = Paginator(articles,2) # 实例化分页对象
    page = request.GET.get('page') # 页号
    try:
        articles = paginator.page(page)
    except PageNotAnInteger: # 传的不是数字 默认显示第一页
        articles = paginator.page(1)
    except EmptyPage: # 没有这个页
        articles = paginator.page(paginator.num_pages) # 越界问题 显示最后一页

    # 设置分页规则
    if page and page.isdigit():
        page = int(page)
    else: # 非法请求分页 则显示第一页
        page = 1
    page_range = paginator.page_range
    if page > 2:
        page_range = list(page_range)[page-2:page+2]
    else:
        if len(page_range) >= 5:
            page_range = list(page_range)[0:5]
        else:
            page_range = list(page_range)[0:len(page_range)]
    # 获取用户信息
    suser = User.objects.get(id=uid)
    showe = 0
    if user.id and suser.id:
        if int(user.id) == int(suser.id):
            showe = 1
    # 获取类目信息
    cats = suser.cats.all()
    return render_to_response('list.html',{'articles':articles,'page_range':page_range,'suser':suser,'showe':showe,'cats':cats})

# 博客内容页
def topic(request,id):
    c = csrf(request)
    article = Article.objects.get(id=id)
    # 获取文章评论内容
    comments = article.comments.all()
    return render_to_response('topic.html',{'article':article,'c':c,'comments':comments})

# 博客评论内容
def art_comment(request):
    if request.method == 'POST':
        content = request.POST.get('content',None)
        art_id = request.POST.get('art_id',None)
        c = comment()
        c.content = content
        c.art = Article(id=art_id)
        c.save()
        return HttpResponseRedirect('/topic_%s' % art_id)

#博客编辑页
def edit(request,id):
    user = request.user
    c = csrf(request)
    if request.method == 'POST':
        title = request.POST.get('title',None)
        content = request.POST.get('content',None)
        cat_id = request.POST.get('cat_id',None)
        if title and content:
            art = Article(id=id,user_id=user.id)
            art.title = title
            art.content = content
            art.cat_id = cat_id
            art.save()
            return HttpResponseRedirect('/art_list_%s_%s/' % (user.id,cat_id)) # 添加成功跳转列表页
        else:
            return render_to_response('error.html',{'e':'标题或者内容不能为空'}) # 添加错误 到错误页面
    art = Article.objects.get(id=id) # 拿到一个博客内容
    cats = cat.objects.filter(user_id=user.id).all() # 获取分类类目
    return render_to_response('edit.html',{'c':c,'art':art,'cats':cats})

def search(request):
    wd = request.GET.get('wd',None)
    articles = Article.objects.filter(title__contains = wd).all()
    return render_to_response('list.html',{'articles':articles})

#首页
def index(request):
    if request.user.is_authenticated():     #判断用户是否已登录
        user = request.user
        return render_to_response('index.html',{'user':user})
    else:
        return render_to_response('index.html')