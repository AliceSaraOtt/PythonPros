# -*- coding:utf-8 -*-
from time import sleep,ctime
import threading

task = [1,2,3,4,5]

def loop(n,second):
    print '睡觉',n + 1,'开始'
    sleep(second)
    print '睡觉',n + 1,'结束'

print ctime()
threads = []
for k,v in enumerate(task):
    t = threading.Thread(target=loop,args=(k,v))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join() # 在线程启动以后调用，起到挂起作用，如果线程没执行完毕，则进程阻塞（暂停）

print ctime()
print '睡醒了'