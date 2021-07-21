from collections import deque

# 상하좌우
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    # ans = 100000000
    found = False
    q = deque()
    q.append((0, 0, 1))
    visited = [[[0] * m for _ in range(n)] for _ in range(2)]

    while q:
        x, y, ham = q.popleft()
        if x == n-1 and y == m-1:
            found = True
            continue

        for i in range(4):
            nx = dr[i] + x
            ny = dc[i] + y
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1 and ham == 1 and visited[ham][nx][ny] == 0:
                    visited[0][nx][ny] = visited[ham][x][y] + 1
                    q.append((nx, ny, 0))
                elif arr[nx][ny] == 0 and visited[ham][nx][ny] == 0:
                    visited[ham][nx][ny] = visited[ham][x][y] + 1
                    q.append((nx, ny, ham))

    if found:
        ans1 = visited[0][n-1][m-1]
        ans2 = visited[1][n-1][m-1]
        # print(ans1, ans2)
        if ans1 != 0 and ans1 < ans2:
            # print(ans1)
            return ans1 + 1
        elif ans1 != 0 and ans2 == 0:
            return ans1 + 1
        elif ans2 != 0:
            # print(ans2)
            return ans2 + 1
    else:
        return -1


n, m = map(int, input().split())

arr = [list(map(int, input())) for _ in range(n)]

if n == 1 and m == 1:
    print(1)
else:
    print(bfs())

# found = False
# q = deque()
# q.append((0, 0, 0))
# visited = [[[0] * m for _ in range(n)] for _ in range(2)]
#
# while q:
#     x, y, ham = q.popleft()
#     if x == n - 1 and y == m - 1:
#         found = True
#         continue
#
#     for i in range(4):
#         nx = dr[i] + x
#         ny = dc[i] + y
#         if 0 <= nx < n and 0 <= ny < m:
#             if arr[nx][ny] == 1 and ham == 0 and visited[ham][nx][ny] == 0:
#                 visited[1][nx][ny] = visited[0][x][y] + 1
#                 q.append((nx, ny, 0))
#             elif arr[nx][ny] == 0 and visited[ham][nx][ny] == 0:
#                 visited[ham][nx][ny] = visited[ham][x][y] + 1
#                 q.append((nx, ny, ham))
#
# if found:
#     ans1 = visited[0][n - 1][m - 1]
#     ans2 = visited[1][n - 1][m - 1]
#     # print(ans1, ans2)
#     if ans1 != 0 and ans1 < ans2:
#         # print(ans1)
#         print(ans1 + 1)
#     elif ans1 != 0 and ans2 == 0:
#         print(ans1 + 1)
#     elif ans2 != 0:
#         # print(ans2)
#         print(ans2 + 1)
# else:
#     print(-1)


