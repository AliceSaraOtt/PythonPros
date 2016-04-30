#coding:utf8
from django.shortcuts import render,HttpResponse,render_to_response
# Create your views here.
from models import QQGroup,userProfile
import json,datetime,common

whole_dict = {}

def index(request):
    groups = QQGroup.objects.filter(members=request.user.id).all()
    return render(request,'index.html',{'groups':groups})

def sendMsg(request):
    data = request.POST.get('data',None)
    data = json.loads(data)
    data['time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    contact_type = data['contact_type']
    to_id = int(data['to_id'])
    if contact_type == 'single': # 一对一聊天
        if to_id not in whole_dict:
            whole_dict[to_id] = common.Chat()
        try:
            whole_dict[to_id].msg_queue.put(data)
            return HttpResponse('ok')
        except Exception , e:
            return HttpResponse('no ok')
    elif contact_type == 'group':
        group_id = data['to_id']
        group = QQGroup.objects.get(id=group_id) # 获取组
        # 获取消息来源人的用户名
        data['from_name'] = userProfile.objects.get(id=data['from_id']).name
        data['from_id'] = group_id # 设置组id
        # 添加消息到每个组成员消息队列中

        for u in group.members.select_related():
            if u.id not in whole_dict:  # u 是一个userprofile对象
                whole_dict[u.id] = common.Chat()
            try:
                if u.id != int(request.user.id):
                    whole_dict[u.id].msg_queue.put(data)
            except Exception ,e:
                return HttpResponse(str(e))
        return HttpResponse('ok')

def getMsg(request):
    uid = request.GET.get('uid',None)
    uid = int(uid)
    res = []
    if uid:
        if uid not in whole_dict:
            whole_dict[uid] = common.Chat()
        res = whole_dict[uid].getMsg()
    return HttpResponse(json.dumps(res))