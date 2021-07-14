import collections

# dc = [0, 1, 1]
# dr = [1, 0, 1]


# def dfs():
#     q = collections.deque()
#     q.append((0, 0))
#     answer = 0
#     while q:
#         now_x, now_y, candy = q.popleft()
#         if now_x == n-1 and now_y == m-1:
#             answer = max(answer, candy)
#         for i in range(3):
#             next_x, next_y = now_x+dc[i], now_y+dr[i]
#             if next_x < n and next_y < m:
#                 q.append((next_x, next_y, candy+arr[next_x][next_y]))
#     return answer

def dp():
    for i in range(n):
        for j in range(m):
            if 0 < i and 0 < j:
                data[i][j] = max(data[i-1][j], data[i][j-1], data[i-1][j-1]) + arr[i][j]
            elif j == 0 and 0 < i:
                data[i][j] = data[i-1][j] + arr[i][j]
            elif i == 0 and 0 < j:
                data[i][j] = data[i][j-1] + arr[i][j]
    return data[n-1][m-1]


n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
data = [[0] * m for _ in range(n)]
data[0][0] = arr[0][0]

# print(dfs())
print(dp())