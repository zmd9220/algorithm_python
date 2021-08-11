
dc = [0, 0, -1, 1]
dr = [-1, 1, 0, 0]


def dfs(x, y):
    st = [(x, y)]
    max_length = 0
    while st:
        nowX, nowY= st.pop()
        # visited[nowX][nowY] = 1
        if arr[nowX][nowY] == 1:
            arr[nowX][nowY] = 0
            max_length += 1
        for i in range(4):
            # if 0 <= nowX+dc[i] < m and 0 <= nowY + dr[i] < n and visited[nowX+dc[i]][nowY + dr[i]] == 0:
            if 0 <= nowX + dc[i] < n and 0 <= nowY + dr[i] < m and arr[nowX + dc[i]][nowY + dr[i]] == 1:
                st.append((nowX+dc[i], nowY+dr[i]))
    return max_length


# 세로 가로
n, m = map(int, input().split())

# 2차원 배열 좌표
arr = [list(map(int, input().split())) for _ in range(n)]
# visited = [0 * m for _ in range(n)]

draw_count = 0
draw_length = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            draw_count += 1
            draw_length = max(draw_length, dfs(i, j))

print(draw_count)
print(draw_length)

