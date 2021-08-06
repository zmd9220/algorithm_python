from collections import deque
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    visited = [[0] * n for _ in range(m)]
    q = deque()
    last_time = 3
    if arr[x-1][y-1]:
        q.append((x-1, y-1, 3))
    else:
        q.append((x-1, y-1, 2))
    while q:
        nx, ny, now_time = q.popleft()
        visited[nx][ny] = 1
        arr[nx][ny] = 0
        if last_time < now_time:
            last_time = now_time
        for i in range(4):
            tx, ty = nx + dr[i], ny + dc[i]
            if 0 <= tx < m and 0 <= ty < n and not visited[tx][ty] and arr[tx][ty]:
                q.append((tx, ty, now_time+1))
    return last_time


n, m = map(int, input().split())
arr = []
for i in range(m):
    tmp = input().strip()
    tmp = list(map(int, tmp))
    # print(tmp)
    arr.append(tmp)
# arr = [list(input()) for _ in range(m)]
# arr2 = list(map(int, input()))
# print(arr2)
y, x = map(int, input().split())

last_zergling = bfs()
live_zergling = 0
for i in range(m):
    for j in range(n):
        if arr[i][j]:
            live_zergling += 1
# print(arr)
print(last_zergling)
print(live_zergling)