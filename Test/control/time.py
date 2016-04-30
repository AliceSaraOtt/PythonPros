# -*- coding: utf-8 -*-
import time as t

#把时间戳转化成时间
def gettime(stamp=None):
    if stamp:
        res = t.strftime('%Y-%m-%d %H:%M:%S',t.gmtime(stamp))
    else:
        res = t.strftime('%Y-%m-%d %H:%M:%S',t.gmtime())
    return res
#print gettime()

#把时间格式字符串转化成时间戳
def getstamp(ftime=None):
    if ftime:
        print ftime
        if ftime.find(' '):
            res = t.mktime(t.strptime(ftime,'%Y-%m-%d %H:%M:%S'))
        else:
            res = t.mktime(t.strptime(ftime,'%Y-%m-%d'))
    else:
        res = t.time()
    return res

print getstamp('2016-10-10')
'''
for i in range(10,0,-1):
    print i
    time.sleep(0.01)
print '睡醒了'
'''