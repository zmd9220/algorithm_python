# 인접행렬로 정점 별 간선 관리로 풀어보기
# dfs를 쓰되 해당 노드 발견시 바로 종료하도록함(리턴?)
# 인덱스 정보는 인접행렬, 방문 여부는 visited를 통해 관리
def dfs(vertexs, edge_list, start, end):
    # 해당하는 정점 수 만큼의 인접 행렬 생성
    arr = [[0] * (vertexs+1) for _ in range(vertexs+1)]
    # 방문여부 확인용
    visited = [0] * (vertexs+1)
    # 스택
    st = []
    # idx 접근하면 복잡하니까 그냥 파이썬 문법으로 편하게 사용
    # for i in range(len(edge_list)):
    #     arr[edge_list[i][0]][edge_list[i][1]] = 1
    #     arr[edge_list[i][1]][edge_list[i][0]] = 1
    # 인접 행렬에 간선 생성 이번 문제에서는 사진으로 볼때 단방향
    for i in edge_list:
        arr[i[0]][i[1]] = 1
    st.append(start)
    while len(st):
        # pop == 현재 노드 위치에 도착 그러므로 방문 확인 배열에도 체크
        vtx = st.pop()
        visited[vtx] = 1
        # 현재 노드 위치가 원하는 목표 노드라면 도착했으므로 종료
        if vtx == end:
            return 1
        # 현재 노드에서 간선으로 연결된 노드들을 추가(다만 방문했으면 굳이 갈 이유가 없으므로 방문 확인 배열에서 체크 확인)
        for i in range(1, vertexs+1):
            if arr[vtx][i] and visited[i] == 0:
                st.append(i)
    # 시작 지점에서 시작하여 갈 수 있는 모든 곳을 돌았으나 목표 노드에 도착하지 못함
    return 0


for t in range(int(input())):
    v, e = map(int, input().split())
    edge_list = []
    for i in range(e):
        x = list(map(int, input().split()))
        edge_list.append(x)
    s, g = map(int, input().split())
    result = dfs(v, edge_list, s, g)
    print('#{} {}'.format(t+1, result))
