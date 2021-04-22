'''
5 6
1 2 1 3 3 2 3 4 2 5 5 4
'''
def bfs(s, v): # 시작점 s, 정점 개수 v
    q = [s]
    visited = [0] * (v+1)
    visited[s] = 1
    while q: # front != rear
        t = q.pop(0)
        print(t) # visit(t), do(t)
        for i in range(1, v+1):
            if adj[t][i] == 1 and visited[i] == 0:
                q.append(i)
                # visited[i] = 1 # 단순 방문 여부만 체크
                visited[i] = visited[t] + 1 # s 로부터 i 까지의 거리 계산


v, e = map(int, input().split())
edge = list(map(int, input().split()))
adj = [[0] * (v + 1) for _ in range(v + 1)]  # 인접 행렬
adjList = [[] for _ in range(v + 1)]  # 인접 리스트
for i in range(e):
    n1 = edge[i * 2]
    n2 = edge[i * 2 + 1]
    adj[n1][n2] = 1  # 인접 행렬
    adj[n2][n1] = 1  # 무향 그래프인 경우 대칭이므로 양방향에 넣어야함 - 방향있는 그래프의 경우 주어지는 데이터의 시작점, 끝점을 잘 파악해서 시작점에만 집어넣어야함

    adjList[n1].append(n2)
    adjList[n2].append(n1)  # 무향인 경우 - 유향인 경우 제외
print()

# 각 정점에서 연결된 노드를 확인하기
for i in range(1, v+1): # i에 인접인 노드
    for j in range(1, v+1):
        if adj[i][j]: # 인접 행렬인 경우
            print(i, j)

    for j in adjList[i]: # 인접 리스트인 경우
        print(i, j)

bfs(1, v)