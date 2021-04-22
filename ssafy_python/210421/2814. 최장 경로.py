
# def dfs(data, start_v, v_size):
#     st = [(start_v, 1)]
#     ans = [1] * (v_size+1)
#     visited = [0] * (v_size+1)
#     while st:
#         v, dst = st.pop(-1)
#         visited[v] = 1
#         if ans[v] < dst:
#             ans[v] = dst
#         for i in range(len(adjList[v])):
#             if visited[adjList[v][i]] == 0:
#                 visited[adjList[v][i]] = 1
#                 st.append((adjList[v][i], dst+1))
#
#     return ans

# 재귀
def dfs2(data, now_v, visit, cnt, ans):

    if ans[now_v] < cnt:
        ans[now_v] = cnt
    for i in adjList[now_v]:
        if visit[i] == 0:
            visit[i] = 1
            dfs2(data, i, visit, cnt+1, ans)
            visit[i] = 0


for t in range(int(input())):
    # n = 정점의 수, m = 간선의 수
    n, m = map(int, input().split())
    # 인접 리스트
    adjList = [[] for _ in range(n+1)] # 1번 인덱스 부터 숫자에 맞게 인덱스 쓸 것
    for i in range(m):
        x, y = map(int, input().split())
        adjList[x].append(y)
        adjList[y].append(x)
    # result = dfs(adjList, 1, n)
    ans2 = [1] * (n+1)

    for i in range(1, n+1):
        visited2 = [0] * (n + 1)
        visited2[i] = 1
        dfs2(adjList, i, visited2, 1, ans2)
    print('#{} {}'.format(t+1, max(ans2)))