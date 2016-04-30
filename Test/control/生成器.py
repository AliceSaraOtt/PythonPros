# -*- coding: utf-8 -*-

def foo1():
    #print '我是一个函数，如果下边出现了yield，我就变成了生成器'
    for i in range(10):
        yield i
g = foo1()
print next(g)
print next(g)
print next(g)
print '-'*40
for i in g:
    print i
print '-'*40
for i in g:
    print i
'''
g = foo1()
i = g.next()
print i
j = g.next()
print j
k = g.next()
print k
g.next()
'''