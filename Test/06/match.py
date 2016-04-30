#coding:utf8
import re_me

str = raw_input('>>>')

#m = re.match(r'^\w+@([a-zA-Z0-9]+\.)+(com|cn)$',str)
#m = re.match(r'[01]{0,1}\d{0,1}\d',str)


if m:
    print '输入合法'
    print m.group()
else:
    print '输入不合法'