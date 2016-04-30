# -*- coding: utf-8 -*-
from time import sleep
import SocketServer

class Human:
    def __init__(self):
        self.height = 100 # 身高
        self.width = 60  # 体重
        self.hp = 100 # 健康值
        self.name = '蛋蛋'
    def eat(self):
        self.width += 10
    def drink(self):
        print '喝'
    def sleep(self):
        sleep(3)
    def hit(self,who):
        who.hp -= 20
    def setName(self,name):
        self.name = name

class Animal(Human):
    def __init__(self):
        self.width = 10
    def run(self):
        print '跑'
    def eat(self):
        print '只能吃草'

class people(Animal):
    # def __init__(self):
    #     self.name = '三季稻'
    #     self.age = 16
    #     self.height = 200
    #     self.width = 400
    #     self.hp = 200

    def __init__(self):
        super(1,self).__init__()
    def play(self):
        print '打游戏'

p1 = people() # 良民
p2 = people() # 暴徒

print p1.width

'''
p1 = Human() # 良民
p2 = Human() # 暴徒
p2.hit(p1)
print 'p1健康值',p1.hp
print 'p2健康值',p2.hp
'''

'''
print p1.width
p1.eat()
print p1.width
'''
