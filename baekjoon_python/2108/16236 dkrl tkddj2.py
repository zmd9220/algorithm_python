from collections import deque
# import pprint
# 상 좌 우 하
dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]


def baby_shark(x, y, size, feed):
    global cnt
    q = deque()
    q.append((x, y, size, feed, 0))
    visited = [[0] * n for _ in range(n)]
    visited[x][y] = 1

    # 성공 배열
    success_x, success_y = 255, 255
    success = []
    # 찾았을 때 가지치기를 위한 bool
    found = False
    # 찾았을 때 해당 움직임 초과는 가지치기 하기 위한 int
    found_move = 0
    while q:
        nx, ny, n_size, n_feed, move = q.popleft()
        # visited[nx][ny] = 1
        # 현재 최소 1번의 먹는 현상이 나타났을 때, 지금 나온 데이터의 움직임이 최초에 먹었던 현상의 움직임보다 크면 더 볼 필요 없음
        # if found and move > found_move:
        #     continue
            # n_feed += 1
            # arr[nx][ny] = 0
            # if n_feed == n_size:
            #     n_feed = 0
            #     n_size += 1

        # if 0 < arr[nx][ny] < n_size:
        #     if nx < success_x or (nx == success_x and ny < success_y):
        #         found = True
        #         found_move = move
        #         success_x, success_y = nx, ny
            # arr2[nx][ny] = (cnt, n_feed, n_size)
            # success.append((nx, ny))

        for i in range(4):
            tx, ty = nx + dr[i], ny + dc[i]
            if 0 <= tx < n and 0 <= ty < n and not visited[tx][ty]:
                if arr[tx][ty] <= n_size or arr[tx][ty] == 0:
                    visited[tx][ty] = 1
                    q.append((tx, ty, n_size, n_feed, move+1))
                if arr[tx][ty] < n_size and arr[tx][ty] != 0:
                    # found = True
                    success.append([tx, ty, move+1])


    # 찾았던 경우 배열 중에서 x축 작은순, y축 작은 순으로 배치
    if success:
        success.sort(key=lambda xx: (xx[2], xx[0], xx[1]))
        # print(success)
        next_x, next_y = success[0][0], success[0][1]
        arr[next_x][next_y] = 0
        # arr[success_x][success_y] = 0
        feed += 1
        if feed == size:
            feed = 0
            size += 1
        cnt += success[0][2]
        # return baby_shark(success_x, success_y, size, feed)
        return baby_shark(next_x, next_y, size, feed)


n = int(input())
cnt = 0
arr = [list(map(int, input().split())) for _ in range(n)]
arr2 = [[0] * n for _ in range(n)]

for i in range(n):
    flag = False
    for j in range(n):
        if arr[i][j] == 9:
            arr[i][j] = 0
            baby_shark(i, j, 2, 0)
            flag = True
            break
    if flag:
        break
print(cnt)
# pprint.pprint(arr2)