# -*- coding:utf-8 -*-
import datetime as dt
t1 = dt.timedelta(days = 365)
t2 = dt.timedelta(weeks=40, days=84, hours=23,minutes=50, seconds=600)

if t1 == t2:
    print '都是一年'
else:
    print '不一样'
print t1.days

print '2017-06-16 23:59:59' > '2017-06-16 00:59:58'

