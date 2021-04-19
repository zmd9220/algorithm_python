
def merge_sort(data):

    if len(data) == 1:
        return data
    mid = len(data) // 2
    left = data[0:mid]
    right = data[mid:len(data)]
    merge_sort(left)
    merge_sort(right)
    return merge(left, right)


def merge(left, right):
    result = []
    global left_first
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif len(left) > 0:
            left_first += 1
            while len(left):
                result.append(left.pop(0))
        elif len(right) > 0:
            while len(right):
                result.append(right.pop(0))
    return result


for t in range(int(input())):
    n = int(input())
    left_first = 0
    arr = list(map(int, input().split()))
    sorted_arr = merge_sort(arr)

    print(arr, sorted_arr, left_first)