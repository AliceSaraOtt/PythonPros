# -*- coding:utf-8 -*-
import re

id = raw_input('input')

# m = re.match(r'(\w+@((\w)+.)+(cn|com))$',id)

# m = re.match(r'^(([0-1]?\d?\d|2[0-4]\d|25[0-5])\.){3}([0-1]?\d?\d|2[0-4]\d|25[0-5])$',id)

# 0-255

if m:
    print m.group()
else:
    print '不合法'