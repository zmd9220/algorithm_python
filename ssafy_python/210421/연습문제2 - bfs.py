# for 문으로 구현 - q로 먼저 만나는 정점 순으로 먼저 탐색
# bfs 는 매번 만나는 정점을 우선으로 진행해야하므로 끝까지 갔다가 돌아오는 재귀 방식으로는 구현 불가
def bfs(data, now_v, v_size): # data - 인접 리스트나 인접 행렬, now_v - 시작점, v_size - 정점 개수
    q = [now_v] # 큐
    visited = [0] * (v_size + 1) # 방문 체크 배열
    while q: # !q.isEmpty()
        vtx = q.pop(0) # 현재 정점 위치 - 큐 이므로 꺼낼때 맨 앞을 꺼내야함
        visited[vtx] = 1
        print(vtx) # visit(v), do(v) - 요구사항에 맞게 처리할 것 처리
        # 내가 가진 간선들을 쭉 둘러보면서 방문 안된 곳이 있으면 큐에 추가
        # 인접 행렬
        # for i in range(1, v_size+1):
        #     if adj[vtx][i] == 1 and visited[i] == 0:
        #         q.append(i)
        #         # 스택에 이미 넣어서 방문 예정이므로 1 - 스택에 중복 방지를 위함
        #         visited[i] = 1
        # 인접 리스트 방식 adjList[v][i]는 이미 내가 가진 간선임이 확실하므로 체크 필요 x
        for i in adjList[vtx]:
            if visited[i] == 0:
                q.append(i)
                # 스택에 이미 넣어서 방문 예정이므로 1 - 스택에 중복 방지를 위함
                # visited[i] = 1
                # bfs만 가능한 부분 - visited에 아예 최단 거리를 구할 수 있다 - 가중치 없을 때의 단순 최소 이동 횟수
                visited[i] = visited[vtx] + 1


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

bfs(adjList, 1, v)

