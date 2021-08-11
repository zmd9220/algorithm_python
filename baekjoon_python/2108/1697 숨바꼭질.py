import collections


def dp(st, end):
    q = collections.deque()
    q.append(st)
    while q:
        tmp = q.popleft()
        if tmp == end:
            return arr[tmp]
        if 0 < tmp and arr[tmp-1] == 100001:
            arr[tmp-1] = arr[tmp]+1
            q.append(tmp - 1)
        if tmp < 100000 and arr[tmp+1] == 100001:
            arr[tmp+1] = arr[tmp]+1
            q.append(tmp + 1)
        if tmp * 2 <= 100000 and arr[tmp*2] == 100001:
            arr[tmp*2] = arr[tmp]+1
            q.append(tmp * 2)

    return arr[end]
# if arr[tmp-1] == 100001 else min(arr[tmp-1], arr[tmp]+1)

n, k = map(int, input().split())

arr = [100001] * 100001

arr[n] = 0

answer = dp(n, k)
print(answer)