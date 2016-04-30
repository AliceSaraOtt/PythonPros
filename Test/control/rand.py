# -*- coding:utf-8 -*-
import random as r
#print r.randint(1,10)
#print r.random()
#print r.randrange(1,10,2)

alpha = [chr(i) for i in range (48,123) if 48<=i<=57 or 65<=i<=90 or 97<=i<=122]

def getCode(num):
    res = ''
    for i in range(0,num): # 循环生成的验证码个数
        rnum = r.randint(0,len(alpha) - 1)
        res += alpha[rnum]
    return res

print getCode(4)

