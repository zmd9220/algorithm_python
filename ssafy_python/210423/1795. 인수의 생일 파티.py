import heapq

inf = 1000000

def dijkstra(n, x, adj, d):
    for i in range(n+1): # 출발지로 부터의 비용
        d[i] = adj[x][i]
    v = [0] * (n+1)
    v[x] = 1 # 출발지 비용 확정
    # 남은 노드 동안 반복
    # q = heapq
    for _ in range(n-1):
        min_idx = 0
        for i in range(1, n+1):
            # 남은 노드 중 비용이 최소인 노드
            if v[i] == 0 and d[i] < d[min_idx]:
                min_idx = i
        # 해당 위치는 비용 확정
        v[min_idx] = 1
        # min_idx 주변 노드들에 대해 최소 비용이 갱신 가능한지 재확인
        for i in range(1, n+1):
            if min_idx != i and adj[min_idx][i] < inf:
                d[i] = min(d[i], d[min_idx]+adj[min_idx][i])


for t in range(int(input())):
    # n 정점, m 간선, x 출발지 겸 도착지
    n, m, x = map(int, input().split())
    # nodes = [list(map(int, input().split())) for _ in range(m)]
    # 문제의 간선은 단방향임
    # adjList = [[] for _ in range(n+1)]
    # 먼저 인접행렬로 풀어보기
    adj = [[inf] * (n+1) for _ in range(n+1)]

    for i in range(n+1):
        # 본인 정점에서 본인 정점은 0임
        adj[i][i] = 0
    for i in range(m):
        # n1 -> n2 까지의 w 가중치
        n1, n2, w = map(int, input().split())
        # adjList[n1].append((n2, w))
        adj[n1][n2] = w
    # 행과 열 바꾸기 버전 1
    # col_adj = [[] for _ in range(n+1)]
    # for i in range(n+1):
    #     for j in range(n+1):
    #         col_adj[i].append(adj[j][i])
    # 버전 2
    col_adj = list(map(list, zip(*adj)))
    # print(adj)
    # print(col_adj)
    d1 = [inf] * (n+1)
    d2 = [inf] * (n+1)
    dijkstra(n, x, adj, d1)
    dijkstra(n, x, col_adj, d2)
    ans = 0
    for i in range(1, n+1):
        if d1[i] + d2[i] > ans:
            ans = d1[i] + d2[i]
    print('#{} {}'.format(t+1, ans))
