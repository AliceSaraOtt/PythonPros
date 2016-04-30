# -*- coding:gbk -*-
import os,sys
#print sys.path
#print os.getcwd()
os.chdir(r'C:\Users\Tina\Desktop\python')
#os.makedirs(r'test\python\1407b')
#os.removedirs(r'test')


#dir =  os.listdir(os.getcwd())

'''
for i in dir:
    if os.path.isdir(i): # os.path.isfile
        dir_i = os.listdir(i)
    print dir_i
'''

g = os.walk(os.getcwd())

for path,dir,filelist in g:
    for filename in filelist:
        print os.path.join(path,filename)
        os.path.isdir()