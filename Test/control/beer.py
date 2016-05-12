#coding:utf8
'''
兜里有10块钱，一瓶啤酒一块钱，两个空瓶子可以换一瓶啤酒，问总共能喝多少瓶啤酒？

啤酒2元一瓶，4个盖换一瓶，2个瓶换一瓶，10元钱最多喝多少瓶？

'''

beer = 0 # 剩余瓶数
money = 100 # 初始金钱
price = 2 # 单价
cap = 0 # 盖
bottle = 0 # 空瓶
beer += money/price

i = 1
while beer != 0:
    print '喝的第%d瓶' % i
    i += 1
    beer -= 1
    cap += 1
    bottle += 1
    if cap == 4:
        cap = 0
        beer += 1
    if bottle == 2:
        bottle = 0
        beer += 1
