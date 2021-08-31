import sys
direction = [(0, 1), (1, 1), (1, 0)]


def dfs(data):
    x, y, dir = data[0], data[1], data[2]
    if x == y == n-1:
        global answer
        answer += 1
        return
    for i in range(3):
        if dir == 0 and i == 2:
            continue
        elif dir == 2 and i == 0:
            continue
        nx, ny = x + direction[i][0], y + direction[i][1]
        if i != 1 and nx < n and ny < n and not arr[nx][ny]:
            dfs([nx, ny, i])
        elif i == 1 and nx < n and ny < n and not arr[nx][ny] and not arr[nx][y] and not arr[x][ny]:
            dfs([nx, ny, i])


def dfs2(x, y, dir):
    if x == y == n-1:
        global answer
        answer += 1
        return
    if dir == 0 or dir == 2:
        if y + 1 < n and not arr[x][y+1]:
            dfs2(x, y+1, 0)
    if dir == 1 or dir == 2:
        if x + 1 < n and not arr[x+1][y]:
            dfs2(x+1, y, 1)
    if dir == 0 or dir == 1 or dir == 2:
        if x + 1 < n and y + 1 < n:
            if arr[x+1][y] == 0 and arr[x][y+1] == 0 and arr[x+1][y+1] == 0:
                dfs2(x+1, y+1, 2)
    # for i in range(3):
    #     if dir == 0 and i == 2:
    #         continue
    #     elif dir == 2 and i == 0:
    #         continue
    #     nx, ny = x + direction[i][0], y + direction[i][1]
    #     if i != 1 and nx < n and ny < n and not arr[nx][ny]:
    #         dfs2(nx, ny, i)
    #     elif i == 1 and nx < n and ny < n and not arr[nx][ny] and not arr[nx][y] and not arr[x][ny]:
    #         dfs2(nx, ny, i)

# def dp():
#     data = [[0] * n for _ in range(n)]
#     for i in range(1, n):
#         if arr[0][i] == 1:
#             break
#         data[0][i] = 1
#     for i in range(1, n):
#         if arr[i-1][2] == 1 or arr[i][1] == 1 or arr[i-1][1] == 1:
#             break
#         data[i][2] = 1
#     # for i in range(3, n):
#     #     data[1][i] = 2
#     for i in range(1, n):
#         for j in range(3, n):
#             for k in range(3):
#                 nx, ny = i - direction[k][0], j - direction[k][1]
#                 if i == 1:
#                     if j ==
#     da = [(0, 1, 0)]
#     while da:
#         x, y, dir = da.pop()
#         if x == y == n-1:
#             global answer
#             answer += 1
#             return
#         for i in range(3):
#             if dir == 0 and i == 2:
#                 continue
#             elif dir == 2 and i == 0:
#                 continue
#             nx, ny = x + direction[i][0], y + direction[i][1]
#             if i != 1 and nx < n and ny < n and not arr[nx][ny]:
#                 da.append([(nx, ny, i)])
#             elif i == 1 and nx < n and ny < n and not arr[nx][ny] and not arr[nx][y] and not arr[x][ny]:
#                 da.append([(nx, ny, i)])

n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# st = [(0, 1, 0)]
st = [0, 1, 0]
answer = 0
if arr[n-1][n-1] == 1:
    print(0)
else:
    dfs2(0, 1, 0)
    print(answer)

# import sys
# N = int(sys.stdin.readline())
# dev = {'hor':(0,1,'hor'),'ang':(1,1,'ang'),'ver':(1,0,'ver')}
# house = []
# dp = [[{'hor':0, 'ang':0, 'ver':0} for _ in range(N+1)]]
# for x in range(N):
#     house.append(list(map(int, sys.stdin.readline().split())))
#     dp.append([{'hor':0, 'ang':0, 'ver':0} for _ in range(N+1)])
#
# dp[1][2]['hor'] = 1
#
# for x in range(1, N+1):
#     for y in range(1, N+1):
#         if (x, y) in [(1, 1), (1, 2)]: continue
#         if not house[x-1][y-1]:
#             dp[x][y]['hor'] = dp[x][y-1]['hor'] + dp[x][y-1]['ang']
#             dp[x][y]['ver'] = dp[x-1][y]['ver'] + dp[x-1][y]['ang']
#             if not (house[x-2][y-1] or house[x-1][y-2]):
#                 dp[x][y]['ang'] = dp[x-1][y-1]['hor'] + dp[x-1][y-1]['ang'] + dp[x-1][y-1]['ver']
#
# print(sum(list(dp[N][N].values())))