# for 문으로 구현 - 갈림길을 스택 이용
def dfs(data, now_v, v_size): # data - 인접 리스트나 인접 행렬, now_v - 시작점, v_size - 정점 개수
    st = [now_v] # 스택
    visited = [0] * (v_size + 1) # 방문 체크 배열
    while st: # !st.isEmpty()
        vtx = st.pop() # 현재 정점 위치 = st.pop(-1)
        visited[vtx] = 1
        print(vtx) # visit(v), do(v) - 요구사항에 맞게 처리할 것 처리
        # 내가 가진 간선들을 쭉 둘러보면서 방문 안된 곳이 있으면 스택에 추가
        # 인접 행렬
        # for i in range(1, v_size+1):
        #     if adj[vtx][i] == 1 and visited[i] == 0:
        #         st.append(i)
        #         # 스택에 이미 넣어서 방문 예정이므로 1 - 스택에 중복 방지를 위함
        #         visited[i] = 1
        # 인접 리스트 방식 adjList[v][i]는 이미 내가 가진 간선임이 확실하므로 체크 필요 x
        for i in adjList[vtx]:
            if visited[i] == 0:
                st.append(i)
                # 스택에 이미 넣어서 방문 예정이므로 1 - 스택에 중복 방지를 위함
                visited[i] = 1
        # 만약 특정 루트로 가기위한 모든 루트 경우의 수를 구한다면 - DFS만 가능한 부분
        # 현재 내가 구할 수 있는 모든 방법을 구하고 다른 루트에서 사용 가능하도록 내 방문 체크인 visited[v]를 해제
        # visited[v] = 0

# 재귀
def dfs2(data, now_v, visit):
    visit[now_v] = 1
    print(now_v)
    for i in adjList[now_v]:
        if visit[i] == 0:
            dfs2(data, i, visit)


edges = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7] # 간선 정보
v = 7 # 정점 갯수
adj = [[0] * (v+1) for _ in range(v+1)] # 인접 행렬 방법
adjList = [[] * (v+1) for _ in range(v+1)] # 인접 리스트 방법
for i in range(0, len(edges), 2):
    start_v = edges[i] # 시작점
    end_v = edges[i+1] # 도착점

    # 인접 행렬
    adj[start_v][end_v] = 1 # 무향, 유향 모두 추가
    adj[end_v][start_v] = 1 # 무향일 때만 추가

    # 인접 리스트
    adjList[start_v].append(end_v) # 무향, 유향일 때 모두 추가
    adjList[end_v].append(start_v) # 무향일 때만

dfs(adjList, 1, v)
visit = [0] * (v+1)
dfs2(adjList, 1, visit)