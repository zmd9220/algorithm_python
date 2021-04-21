
# def bfs(s, v): # 시작점 s, 정점 개수 v
#     q = [s]
#     visited = [0] * (v+1)
#     visited[s] = 1
#     while q: # front != rear
#         t = q.pop(0)
#         print(t) # visit(t), do(t)
#         for i in range(1, v+1):
#             if adj[t][i] == 1 and visited[i] == 0:
#                 q.append(i)
#                 visited[i] = 1

