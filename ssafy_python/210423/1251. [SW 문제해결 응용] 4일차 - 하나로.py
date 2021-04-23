def find_set(num):
    if num != make_sets[num]:
        make_sets[num] = find_set(make_sets[num])
    return make_sets[num]

def kruskal(n, edge):

    mst = 0
    values = 0
    while mst != n-1:
        w, v, u = edge.pop()
        if find_set(v) != find_set(u):
            make_sets[find_set(u)] = find_set(v)
            mst += 1
            values += w
    return values


for t in range(int(input())):
    n = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    e = float(input())
    # adj = [[0] * n for _ in range(n)]
    # adjList = [[] * n for _ in range(n)]
    adjList = []
    # 각 간선 별 가중치 계산
    # 인접 행렬 버전
    # for i in range(n):
    #     for j in range(n):
    #         if adj[i][j] == 0:
    #             w = abs(x_list[i]-x_list[j])**2 + abs(y_list[i]-y_list[j])**2
    #             adj[i][j] = w
    #             adj[j][i] = w
    # 인접 리스트 버전
    for i in range(n):
        for j in range(i+1, n):
            w = abs(x_list[i]-x_list[j])**2 + abs(y_list[i]-y_list[j])**2
            # adjList[i].append((j, w))
            # adjList[j].append((i, w))
            adjList.append((w, i, j))
    adjList.sort(reverse=True)
    # 상호 배타 집합
    make_sets = [i for i in range(n)]
    ans = kruskal(n, adjList)
    print('#{} {}'.format(t+1, round(ans*e)))

