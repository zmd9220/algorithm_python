# binary search - 재귀, 반복
def binary_search(base_arr, search_arr):
    cnt = 0
    for i in range(len(search_arr)):
        start = 0
        end = len(base_arr) - 1
        # find_val = search_arr[i]
        # 1 - 우측 0 - 왼쪽
        now_flag = 2
        before_flag = 3
        while start <= end:
            mid = (start + end) // 2
            if base_arr[mid] == search_arr[i]:
                cnt += 1
                break
            elif base_arr[mid] > search_arr[i]:
                end = mid - 1
                # mid = (start+end) // 2
                now_flag = 0
            elif base_arr[mid] < search_arr[i]:
                start = mid+1
                now_flag = 1
            if before_flag == now_flag:
                break
            before_flag = now_flag

    return cnt


for t in range(int(input())):
    n, m = map(int, input().split())
    arr_n = sorted(list(map(int, input().split())))
    arr_m = list(map(int, input().split()))
    ans = binary_search(arr_n, arr_m)
    print('#{} {}'.format(t+1, ans))
