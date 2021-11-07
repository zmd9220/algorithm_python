
def quick_sort(arr, st, end):
    if st >= end:
        return
    pivot = st
    right = end
    left = st+1
    while right >= left:
        while arr[left] < arr[pivot]:
            left += 1
        while arr[right] > arr[pivot]:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            break
    arr[pivot], arr[right] = arr[right], arr[pivot]
    quick_sort(arr, 0, right-1)
    quick_sort(arr, right+1, end)


'''
12명이 모두 악수하는 경우의 수
m*(m - 3) / 2 = 다각형에서의 대각선의 갯수
12 * 9 / 2 = 66
12c2 = 66
11 + 10 + ... + 1 = m*(m+1) / 2

1 11
2 10
3 9
4 8
5 7
6 6
7 5
8 4
9 3
10 2
11 1
'''