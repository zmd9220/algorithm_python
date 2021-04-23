
inf = 100000001

def dijkstra():
    return

for t in range(int(input())):
    # n 정점, m 간선, x 출발지 겸 도착지
    n, m, x = map(int, input().split())
    # nodes = [list(map(int, input().split())) for _ in range(m)]
    # 문제의 간선은 단방향임
    adjList = [[] for _ in range(n+1)]
    # 먼저 인접행렬로 풀어보기
    adj = [[inf] * (n+1) for _ in range(n+1)]

    for i in range(n+1):
        # 본인 정점에서 본인 정점은 0임
        adj[i][i] = 0
    for i in range(m):
        # n1 -> n2 까지의 w 가중치
        n1, n2, w = map(int, input().split())
        adjList[n1].append((n2, w))
        adj[n1][n2] = w
    # 행과 열 바꾸기 버전 1
    # col_adj = [[] for _ in range(n+1)]
    # for i in range(n+1):
    #     for j in range(n+1):
    #         col_adj[i].append(adj[j][i])
    # 버전 2
    col_adj = list(map(list, zip(*adj)))
    print(adj)
    print(col_adj)