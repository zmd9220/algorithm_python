

# http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=2857&sca=3010
def binary_search(data, low, high, target):
    while low <= high:
        mid = (low+high) // 2
        if data[mid] == target:
            return mid
        if data[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def binary_search2(data, low, high, target):
    if low > high:
        return -1
    mid = (low + high) // 2

    if data[mid] == target:
        return mid

    if data[mid] > target:
        return binary_search2(data, low, mid-1, target)
    return binary_search2(data, mid+1, high, target)


n = int(input())
arr = list(map(int, input().split()))
q = int(input())
question = list(map(int, input().split()))

for i in range(q):
    # found = False
    # low, high = 0, n-1
    # answer = -1
    # while low <= high:
    #     mid = (low+high) // 2
    #     if arr[mid] == question[i]:
    #         # found = True
    #         answer = mid
    #         break
    #     if arr[mid] > question[i]:
    #         high = mid - 1
    #     else:
    #         low = mid + 1
    # print(answer, end=' ')
    # print(binary_search(arr, 0, n-1, question[i]), end=' ')
    print(binary_search2(arr, 0, n-1, question[i]), end=' ')

