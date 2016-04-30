# -*- coding:utf-8 -*-
class Guai:
    def __init__(self):
        print '我是初始化,我在创造怪的时候自动被调用一次'
        self.hp = 1000
    def yao(self,ren):
        ren.hp -= 1

class Fashi: # 法师模子 一个类
    gongji = 10
    fangyu = 5
    hp = 100 # 血量
    def att(self,guai): #普通攻击
        guai.hp -= self.gongji
    def huoqiushu(self,guai):
        guai.hp -= 1000
    def hanbingjian(self):
        print '防御能力'
    def setGongji(self,d):
        self.gongji += d

g1 = Guai()
print g1.hp

'''

f1 = Fashi() # 创造了一个法师
print '法师1号的血量是：',f1.hp
f2 = Fashi() # 又创造了一个法师
print '法师2号的血量是：',f2.hp
f1.setGongji()

g1 = Guai() #创造了一个怪
g1.yao(f1)
print '-'*20

print '法师1号的血量是：',f1.hp
f2 = Fashi() # 又创造了一个法师
print '法师2号的血量是：',f2.hp



g1 = Guai() #创造了一个怪
f1.setGongji(10)
print f1.gongji
exit()

f1.att(g1) #对怪1普通攻击
f1.huoqiushu(g1)  #对怪1 释放火球术


if g1.hp <= 0:
    print '怪死了'
'''


