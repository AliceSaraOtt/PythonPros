# -*- coding:utf-8 -*-
def foo(s):
    if s == '':
        return False
    elif not s.isdigit():
        return False
    return True
s = raw_input()

if foo(s):
    print '验证通过'
else:
    print '不合法'