#coding:utf8
from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from qq.models import UserProfile,QQgroup
from django.db import connection
import json,datetime,Queue
from dwebsocket import require_websocket

# Create your views here.

whole_dict = {}

# 构造 1:对象,2:Player(),3:Player()

class Player:
    def __init__(self):
        self.msg_q = Queue.Queue()
    def getMsg(self):
        msgs = []
        if self.msg_q.qsize() > 0: # 有消息的情况下
            for msg in range(self.msg_q.qsize()):
                msgs.append(self.msg_q.get())
        else:
            try:
                msgs.append(self.msg_q.get(timeout=30))
            except Queue.Empty:
                return msgs
            except Exception ,e:
                print '客户端已断开连接'
        return msgs

@login_required()
def home(req):
    # friends = req.user.userprofile.friend.select_related()
    # fids = []
    # for f in friends:
    #     fids.append(f.id)
    # test = UserProfile.objects.exclude(id__in=fids)

    # 获取组
    groups = QQgroup.objects.filter(member=req.user.userprofile.id).all()
    return render(req,'qq/home.html',{'groups':groups})

def sendMsg(req):
    data = req.POST.get('data')
    data = json.loads(data)
    data['time'] = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    contact_type = data['contact_type']
    to_id = int(data['to_id'])
    if contact_type == 'single': # 单人聊天
        if to_id not in whole_dict:
            whole_dict[to_id] = Player()
        try:
            whole_dict[to_id].msg_q.put(data)
            return HttpResponse('ok')
        except Exception,e:
            return HttpResponse(str(e))
    elif contact_type == 'group': # 群组聊天
        group_id = data['to_id']
        group = QQgroup.objects.get(id=group_id)
        # 获取消息来源人的用户名
        group_name = UserProfile.objects.get(id=data['from_id']).name
        data['group_name'] = group_name
        uid = data['from_id']
        data['from_id'] = group_id

        for u in group.member.select_related():
            if u.id not in whole_dict:
                whole_dict[u.id] = Player()
            try:
                if int(u.id) != int(uid):
                    # print u.id
                    whole_dict[u.id].msg_q.put(data)
            except Exception , e:
                return HttpResponse(str(e))
        return HttpResponse('ok')

def getMsg(req):
    uid = req.GET.get('uid')
    uid = int(uid)
    if uid:
        if uid not in whole_dict:
            whole_dict[uid] = Player()
        msgs = whole_dict[uid].getMsg()
        return HttpResponse(json.dumps(msgs))

@require_websocket
def test(req):
    print req.is_websocket()
    message = req.websocket.wait()
    req.websocket.send('我爱你')



