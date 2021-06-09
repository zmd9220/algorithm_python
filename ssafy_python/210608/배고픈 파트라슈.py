dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(sr, sc, milk, dist, vill):
    global min_path

    if not milk or dist >= min_path:
        if dist < min_path:
            min_path = dist
        return

    for i in range(4):
        nr, nc = sr + dr[i], sc + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            if vill[nr][nc] == 1:
                vill[nr][nc] = 2
                dfs(nr, nc, milk - 1, dist + 1, vill)
                vill[nr][nc] = 1
            elif not vill[nr][nc]:
                vill[nr][nc] = 2
                dfs(nr, nc, milk, dist + 1, vill)
                vill[nr][nc] = 0


for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    vill = [list(map(int, input().split())) for n in range(N)]
    min_path = N ** 2
    dfs(0, 0, M, 0, vill)
    print(f'#{t} {min_path}')