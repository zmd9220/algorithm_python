
from collections import deque

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def bfs(x, y, sts, move):
    if move == 6:
        an.add(sts)
        # if sts not in answer:
        #     answer.append(sts)
        return
    for i in range(4):
        nx, ny = x + dr[i], y + dc[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            bfs(nx, ny, sts + str(arr[nx][ny]), move+1)


arr = [list(map(int, input().split())) for _ in range(5)]
answer = []
an = set()
for i in range(5):
    for j in range(5):
        bfs(i, j, str(arr[i][j]), 1)
# print(len(answer))
# print(answer)
# print(an)
print(len(an))