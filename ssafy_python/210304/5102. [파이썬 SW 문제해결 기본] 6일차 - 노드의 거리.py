def bfs(start, end, data):
    queue = [start]
    distance = [0] * len(data)
    while len(queue):
        now_vtx = queue.pop(0)
        if now_vtx == end:
            return distance[now_vtx]
        else:
            for i in range(1, len(data)):
                if data[now_vtx][i] and distance[i] == 0:
                    queue.append(i)
                    distance[i] += distance[now_vtx] + 1

    return 0


for t in range(int(input())):
    v, e = map(int, input().split())
    arr = [[0] * (v+1) for _ in range(v+1)]
    # 인접행렬 생성
    for i in range(e):
        vtx1, vtx2 = map(int, input().split())
        arr[vtx1][vtx2] = 1
        arr[vtx2][vtx1] = 1
    s, g = map(int, input().split())
    print(f'#{t+1} {bfs(s, g, arr)}')