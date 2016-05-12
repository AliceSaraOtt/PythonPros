# -*- coding:utf-8 -*-
import sys,random
a = [3, 9, -6, -10, -9, -1, 10, -7, 3, 6]
# a = [1,2,-1,-5,3]

# 求散列最大和问题-最笨方法！~
max_num = 0
for i in range(0,4):
    for j in range(i,4):
        total = 0
        for k in range(i,j+1):
            total += a[k]
        if total > max_num:
            max_num = total
print max_num