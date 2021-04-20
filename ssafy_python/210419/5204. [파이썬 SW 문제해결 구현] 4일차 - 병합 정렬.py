
def merge_sort(data):
    if len(data) == 1:
        return data
    mid = len(data) // 2
    left = data[0:mid]
    right = data[mid:len(data)]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(left, right):
    result = []
    left_len = len(left)
    right_len = len(right)
    list_len = left_len + right_len
    global left_first
    left_idx = right_idx = 0
    right_small = False
    for i in range(list_len):
        if left_idx == len(left):
            result.append(right[right_idx])
            right_idx += 1
        elif right_idx == len(right):
            result.append(left[left_idx])
            left_idx += 1
            right_small = True
        elif left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    if right_small:
        left_first += 1
    return result


for t in range(int(input())):
    n = int(input())
    left_first = 0
    arr = list(map(int, input().split()))
    sorted_arr = merge_sort(arr)
    print('#{} {} {}'.format(t+1, sorted_arr[n//2], left_first))
    # print(arr, sorted_arr, left_first)
