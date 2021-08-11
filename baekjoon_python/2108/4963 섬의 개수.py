
dr = [1, -1, 0, 0, 1, 1, -1, -1]
dc = [0, 0, -1, 1, 1, -1, 1, -1]


def dfs(x, y, visit):
    # visit[x][y] = 0
    arr[x][y] = 0
    for i in range(8):
        nx, ny = x + dr[i], y + dc[i]
        if 0 <= nx < h and 0 <= ny < w and arr[nx][ny]:
            dfs(nx, ny, visit)


def dfs2(x, y):
    st = [(x, y)]
    while st:
        tx, ty = st.pop()
        arr[tx][ty] = 0
        for i in range(8):
            nx, ny = tx + dr[i], ty + dc[i]
            if 0 <= nx < h and 0 <= ny < w and arr[nx][ny]:
                st.append((nx, ny))


while True:
    w, h = map(int, input().split())
    if not w and not h:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                visited = [[0] * w for _ in range(h)]
                ans += 1
                # dfs(i, j, visited)
                dfs2(i, j)
    print(ans)