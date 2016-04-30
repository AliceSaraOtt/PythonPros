# coding:utf8

arr = [49, 38, 65, 97, 76, 13, 27, 49, 55, 4]
narr = []


# 选择排序
def bubble(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr


# 冒泡排序
# for j in range(len(arr)):
#     for i in range(len(arr) - 1 - (j + 1)):
#         if arr[i] < arr[i + 1]:
#             arr[i],arr[i+1] = arr[i+1],arr[i]

# 插入排序
for i in range(len(arr)):
    for j in range(i):

print arr
