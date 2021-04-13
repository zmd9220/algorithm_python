def dfs_check_route(edge_list):
    visited = [0] * 100 # 방문 여부
    arr = [[0] * 100 for _ in range(100)] # 인접 행렬
    st = [] # 스택으로 dfs 탐색
    # 만약 4짜리라면 0,2 까지 진행후 4가되면 끝나야 하므로 끝나는것이 3이후여야 끝나야 하므로 그냥 edge_list 전체 크게로 해도됨
    # 해당 간선은 단방향이므로 한 방향만 추가
    for i in range(0, len(edge_list), 2):
        arr[edge_list[i]][edge_list[i+1]] = 1
    st.append(0)
    while len(st):
        # 현재 정점 가져오기 + 방문했음을 체크
        now_vtx = st.pop()
        visited[now_vtx] = 1
        # 99는 도착지
        if now_vtx == 99:
            return 1
        for i in range(100):
            # 해당 정점과 이어진 간선이 있는 정점(i)([now_vtx][i] == 1)이면서 아직 방문한 적이 없는 정점일 때만 추가
            if arr[now_vtx][i] and visited[i] == 0:
                st.append(i)
    return 0


for t in range(1, 11):
    tc, pair = map(int, input().split())
    pairs = list(map(int, input().split()))
    result = dfs_check_route(pairs)
    print('#{} {}'.format(tc, result))