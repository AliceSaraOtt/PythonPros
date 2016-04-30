# -*- coding:utf-8 -*-

def fun1(): # 没有返回值的时候 返回None
    for i in range(101):
        print i

def fun2(num2,num1=10):
    return num1 + num2

def fun3(city):
    n_city = []
    for i in city:
        if i != '广州':
            n_city.append(i)
    return n_city

city = ['哈尔滨','北京','杭州','广州','深圳']

n_city = fun3(city)

for i in n_city:
    print i

'''
def check(str):
    if str == '':
        return False
    elif not str.isdigit():
        return False
    return True

s = raw_input('请输入:')
if check(s):
    print '合法'
else:
    print '不合法'
'''

'''
num1 = raw_input('输入第一个数')
num2 = raw_input('输入第二个个数')
sum = fun2(int(num1),int(num2))
print sum
#fun1()
'''