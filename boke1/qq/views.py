#coding=utf8
import json,datetime,utiles
from django.shortcuts import render,HttpResponse,render_to_response
from models import QQGroup,UserProfile
global_msg_dic = {}

# Create your views here.
def home(request):
    groups = QQGroup.objects.filter(members=request.user.id).all()
    return render(request,'qq/home.html',{'groups':groups})
    #return render_to_response('qq/home.html',{'request':request}) # 渲染的模版中没有request对象

def sendMsg(request):
    data = request.POST.get('data')
    data = json.loads(data)
    data['date'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    to_id = int(data['to_id'])
    contact_type = data['contact_type']
    if contact_type == 'single':
        if not global_msg_dic.has_key(to_id):
            global_msg_dic[to_id] = utiles.Chat()
        global_msg_dic[to_id].msg_queue.put(data)
        print global_msg_dic
    elif data.get('contact_type') == 'group':  # 群组聊天
        group_id = data['to_id']
        group_obj = QQGroup.objects.get(id=group_id)
        data['from_name'] = UserProfile.objects.get(id=data['from_id']).name
        data['from_id'] = group_id

        for u in group_obj.members.select_related():
            if not global_msg_dic.has_key(u.id):
                global_msg_dic[u.id] = utiles.Chat()

            if int(request.user.id) != u.id:
                global_msg_dic[u.id].msg_queue.put(data)
    return HttpResponse(data)

def getMsg(request):
    uid = request.GET.get('uid',None)
    uid = int(uid)
    if uid:
        res = []
        if not global_msg_dic.has_key(uid):
            global_msg_dic[uid] = utiles.Chat()
        res = global_msg_dic[uid].get_msg()
        return HttpResponse(json.dumps(res))
    else:
        return HttpResponse(json.dumps('uid wrong'))