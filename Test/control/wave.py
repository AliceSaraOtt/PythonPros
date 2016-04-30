# for i in range(3):
#     for j in range(3):
#         if j <= i:
#             print '*',
#     print ''
import random as r,time
# high = r.randint(10)

i = 0
add = 1
edge = 20
high = 10
low = 0
while i < edge:
    j = 0
    while j < edge:
        if j <= i:
            print '*',
            time.sleep(0.05)
        j = j + 1
    if i == high:
        add = 0
        low = r.randint(0,3)
    elif i == low:
        add = 1
        high = r.randint(8,10)
    if add:
        i = i + 1
    else:
        i = i - 1
    print ''