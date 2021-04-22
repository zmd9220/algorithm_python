
def dijkstra(start):
    # 시작 정점 start
    # 인접 행렬 x 리스트 adjList
    # 정점 집합 v ?
    # 최단 거리를 넣을 배열 d
    d = [100000001] * (v)
    # 선택된 정점 집합 u
    u = set()
    u.add(start)
    # u = [start]
    d[start] = 0
    now_v = start
    # 현재 정점에서 갈 수 있는 간선이 해당 정점으로 갈 수 있는 최소 거리보다 작으면 갱신 해주기
    for weight, dst_v in adjList[now_v]:
        if d[dst_v] > d[now_v] + weight:
            d[dst_v] = d[now_v] + weight

    while len(u) != v:
        # 현재 정점 중에서 갈 수 있는 가장 가중치가 낮은 정점을 다음 정점으로 삼아주기 - 나는 정렬해놔서 맨뒤꺼 꺼내기
        # now_weight, now_v = adjList[now_v].pop()
        now_weight = 100000001
        delete_v = None
        for i in u:
            # if not adjList[i]:
            #     continue
            if adjList[i][-1][0] < now_weight and adjList[i][-1][1] not in u:
                now_weight = adjList[i][-1][0]
                now_v = adjList[i][-1][1]
                delete_v = i
        if now_v == v-1:
            return d
        adjList[delete_v].pop()
        u.add(now_v)

        for weight, dst_v in adjList[now_v]:
            d[dst_v] = min(d[dst_v], d[now_v] + weight)
    return d

for t in range(int(input())):
    v, e = map(int, input().split())
    # v = 2 면 노드수는 3개임 0,1,2
    v += 1
    adjList = [[] for _ in range(v)]
    for i in range(e):
        n1, n2, w = map(int, input().split())
        adjList[n1].append((w, n2))
        # adjList[n2].append((w, n1))
    # 미리 정렬해두면 꺼낼때 편할듯 - 간선별 최단거리 꺼낼거니
    for i in range(v):
        adjList[i].sort(key=lambda x: -x[0])
        # adjList[i].sort(reverse=True)
    ans = dijkstra(0)
    # print(ans)
    print('#{} {}'.format(t+1, ans[v-1]))

