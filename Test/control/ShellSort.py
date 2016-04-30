def shell(arr):
    l = len(arr)
    h = 1
    while h < l // 3:
        h = 3 * h + 1
        while h >= 1:
            for i in range(h, l):
                j = i
            while j >= h and arr[j] < arr[j - h]:
                arr[j], arr[j - h] = arr[j - h], arr[j]
            j -= h
            h = h // 3
    return arr

arr = [49, 38, 65, 97, 76, 13, 27, 49, 55, 4]
arr1 = [5,4,3,1,2,3,4]

print shell(arr)

# def shell(arr):
#     l=len(arr)
#     h=1
#     while h<l//3:
#         h=3*h+1
#     while h>=1:
#         for i in range(h,l):
#     j=i
#     while j>=h and arr[j]<arr[j-h]:
#     arr[j],arr[j-h]=arr[j-h],arr[j]
#     j-=h
#     h=h//3
#     return arr
