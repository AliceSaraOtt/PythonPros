arr = [49, 38, 65, 97, 76, 13, 27, 49, 55, 4]

# 选择排序
# for i in range(len(arr)):
#     min = i
#     for j in range(i+1,len(arr)):
#         if arr[j] < arr[min]:
#             min = j
#     arr[min],arr[i] = arr[i],arr[min]
# print arr

#冒泡排序
for i in range(len(arr)):
    for j in range(len(arr) - 1 - i):
        if arr[j + 1] < arr[j]:
            arr[j+1],arr[j] = arr[j],arr[j+1]

print arr