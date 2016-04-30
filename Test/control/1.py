# -*- coding:utf-8 -*-
china = {
    '北京': {
        '海淀': ['中关村', '五道口']
    },
    '黑龙江': {
        '哈尔滨': ['道理', '道外', '南岗', '香坊', '动力', '平房']
    }
}
def check(pro_i,len): # 验证非空和越界
    if pro_i == '':
        return 1
    if pro_i.isdigit():
        pro_i = int(pro_i)
        if pro_i >= len:
            return 1 #继续循环
        else:
            return
    elif pro_i == 'exit' or pro_i == 'q':
        return 2  # 大退
    elif pro_i == 'back':
        return 3  # 返回上级
    else:
        print '输入不合法：'
        return 1

i = 0
while True:
    if i:
        break
    for k, v in enumerate(china):
        print k, v
    pro_i = raw_input('请输入')
    l_p = len(list(china))
    if check(pro_i,l_p) == 1:
        continue
    elif check(pro_i,l_p) == 2:
        break
    pro_i = int(pro_i)
    city = china[list(china)[pro_i]]
    j = 0
    while True:
        if j:
            break
        for k, v in enumerate(city):
            print '-' * 5, k, v
        city_i = raw_input('请输入')
        l_c = len(list(city))
        if check(city_i,l_c) == 1:
            continue
        elif check(city_i,l_c) == 2:
            i = 1
            break
        elif check(city_i,l_c) == 3:
            break
        city_i = int(city_i)
        area = city[list(city)[city_i]]
        while True:
            for k, v in enumerate(area):
                print '-' * 10, k, v
            bore = raw_input('返回输入：back；退出输入：exit\n')
            if check(bore,len(area)) == 1:
                continue
            elif check(bore,len(area)) == 2:
                i,j = 1,1
                break
            elif check(bore,len(area)) == 3:
                break

