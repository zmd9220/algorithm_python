
def quick_sort(data, pivot, end):
    i, j = pivot+1, end
    if pivot < end:
        while True:
            while i < end and data[i] < data[pivot]:
                i += 1
            while j > pivot and data[j] > data[pivot]:
                j -= 1
            if j <= i:
                data[j], data[pivot] = data[pivot], data[j]
                quick_sort(data, pivot, j-1)
                quick_sort(data, j+1, end)
                break
            else:
                data[j], data[i] = data[i], data[j]
                j -= 1
                i += 1
        return


# def qsort(a, low, high):
#     if low < high:
#         pivot = partition(a, low, high)
#         qsort(a, low, pivot-1)
#         qsort(a, pivot+1, high)
#
#
# def partition(a, pivot, high):
#     i = pivot + 1
#     j = high
#     while True:
#         while i < high and a[i] < a[pivot]:
#             i += 1
#         while j > pivot and a[j] > a[pivot]:
#             j -= 1
#         if j <= i:
#             break
#         a[i], a[j] = a[j], a[i]
#         i += 1
#         j -= 1
#     a[pivot], a[j] = a[j], a[pivot]
#     return j


arr1 = [11, 45, 23, 81, 28, 34]
arr2 = [11, 45, 23, 81, 28, 34, 99, 22, 17, 8]
arr3 = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

arr = [[11, 45, 23, 81, 28, 34], [11, 45, 23, 81, 28, 34, 99, 22, 17, 8],
       [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
       ]

for i in range(3):
    quick_sort(arr[i], 0, len(arr[i])-1)
    # qsort(arr[i], 0, len(arr[i])-1)
    print(arr[i])


