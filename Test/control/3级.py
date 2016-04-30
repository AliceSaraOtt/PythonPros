# -*- coding:utf-8 -*-
china = {
    '北京': {
        '海淀': ['中关村', '五道口']
    },
    '黑龙江': {
        '哈尔滨': {
            '哈尔滨北':['道理', '道外', '南岗'],
            '哈尔滨南':['香坊', '动力', '平房']
            }
    }
}
pro = china.keys() # 省列表
i = 0
while True:
    if i:
        break
    for k,v in enumerate(pro):
        print k,v
    pro_i = raw_input()
    pro_i = int(pro_i)
    city = china[pro[pro_i]] # 城市字典
    citys = city.keys() # 列表
    j = 0
    while True:
        if j:
            break
        for k,v in enumerate(citys):
            print '-'*5 ,k,v
        city_i = raw_input()
        if city_i == 'back':
            break
        elif city_i == 'exit' or city_i == 'q':
            i = 1
            break
        city_i = int(city_i)
        area = city[citys[city_i]] # 字典
        areas = area.keys() # 最后一级列表
        while True:
            for k,v in enumerate(areas):
                print '-'*10,k,v
            area_i = raw_input()
            if area_i == 'back':
                break
            elif area_i == 'exit' or area_i == 'q':
                i,j = 1,1
                break
            area_i = int(area_i)
            final = area[areas[area_i]]
            while True:
                for k,v in enumerate(final):
                    print '-'*15,k,v
                bore = raw_input()
                if bore == 'back':
                    break
                elif bore == 'exit' or bore == 'q':
                    exit()
