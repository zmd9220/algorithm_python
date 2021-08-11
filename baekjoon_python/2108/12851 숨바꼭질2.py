from collections import deque

dc = [-1, +1, *2]

def bfs(st, end):
    q = deque()
    q.append(st)
    cnt = 1
    min_value = 1000001
    while q:
        tmp = q.popleft()

        if arr[tmp] > arr[end]:
            continue

        if 0 < tmp and arr[tmp-1] == 100001:
            arr[tmp-1] = arr[tmp]+1
            q.append(tmp - 1)
        elif 0 < tmp and tmp - 1 == end:
            if arr[tmp] + 1 == arr[end]:
                cnt += 1

        if tmp < 100000 and arr[tmp+1] == 100001:
            if tmp+1 == end:
                arr[end] = arr[tmp] + 1
                cnt = 1
                min_value = arr[tmp] + 1
            else:
                arr[tmp+1] = arr[tmp]+1
                q.append(tmp + 1)
        elif tmp < 100000 and tmp + 1 == end:
            if arr[tmp] + 1 == arr[end]:
                cnt += 1

        if tmp * 2 <= 100000 and arr[tmp*2] == 100001:
            if tmp*2 == end:
                arr[end] = arr[tmp] + 1
                cnt = 1
                min_value = arr[tmp] + 1
            else:
                arr[tmp*2] = arr[tmp]+1
                q.append(tmp * 2)
        elif tmp * 2 <= 100000 and tmp * 2 == end:
            if arr[tmp] + 1 == arr[end]:
                cnt += 1

    return min_value, cnt


n, k = map(int, input().split())

arr = [100001] * 100001

arr[n] = 0

if n == k:
    min_time, min_cnt = 0, 1
else:
    min_time, min_cnt = bfs(n, k)
print(min_time)
print(min_cnt)