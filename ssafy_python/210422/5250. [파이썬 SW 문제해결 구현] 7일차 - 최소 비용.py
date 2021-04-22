
# 다익스트라
# 상하 좌우로 움직이므로 델타
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def dijkstra():
    fuels = [[100000000] * n for _ in range(n)]
    is_min_fuels = [[0] * n for _ in range(n)]
    fuels[0][0] = 0
    delta = set()
    delta.add((0, 0))
    while True:
        min_fuel = 1000000000
        x, y = 0, 0
        # 현재 델타 (방문했던 정점 좌표들) 내에 아직 해당 좌표가 최소 비용이 확정되지 않은 좌표중에서 가장 최소 비용인 정점 좌표를 꺼내기
        for delta_x, delta_y in delta:
            if fuels[delta_x][delta_y] < min_fuel and not is_min_fuels[delta_x][delta_y]:
                min_fuel = fuels[delta_x][delta_y]
                x, y = delta_x, delta_y
        # 해당 좌표를 꺼냈으면 현재 좌표는 최소 거리 확정
        is_min_fuels[x][y] = 1
        delta.remove((x, y))

        # 현재 좌표가 도착 좌표라면 (n-1, n-1) 현재 가진 최소 비용을 리턴
        if x == y == n-1:
            return fuels[x][y]

        # 도착 좌표가 아니라면 다음 지점을 찾기 위해 델타 검색
        for i in range(4):
            next_x, next_y = x+dr[i], y+dc[i]
            # 현재 델타 값을 더한 새로운 좌표가 배열 범위 내이고, 확정되지 않은 좌표라면
            if 0 <= next_x < n and 0 <= next_y < n and not is_min_fuels[next_x][next_y]:
                # 해당 좌표의 연료 계산 (이전 좌표와 높이 차이가 있으면 해당 높이만큼에 +1, 없으면 그냥 +1)
                if arr[x][y] < arr[next_x][next_y]:
                    now_fuel = fuels[x][y] + (arr[next_x][next_y] - arr[x][y]) + 1
                else:
                    now_fuel = fuels[x][y] + 1

                # 만약 이번에 구한 총 연료 비용이 현재 fuels 좌표에 있는 최소 연료 비용보다 작으면 갱신
                if now_fuel < fuels[next_x][next_y]:
                    fuels[next_x][next_y] = now_fuel
                    delta.add((next_x, next_y))


for t in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = dijkstra()
    print('#{} {}'.format(t+1, ans))