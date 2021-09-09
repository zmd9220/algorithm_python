# import pprint
from collections import deque
dr = [1, -1, 0, 0, 1, 1, -1, -1, 0]
dc = [0, 0, -1, 1, -1, 1, -1, 1, 0]

def bfs(x, y, cnt):
    q = deque()
    q.append((x, y, cnt))
    while q:
        nx, ny, n_cnt = q.popleft()
        if flag:
            return 1
        if n_cnt == 8 or (nx == 0 and ny == 7):
            return 1
        if all_arr[n_cnt][nx][ny] == '#':
            continue
        for i in range(9):
            tx, ty = nx + dr[i], ny + dc[i]
            if 0 <= tx < 8 and 0 <= ty < 8 and all_arr[n_cnt][tx][ty] == '.':
                q.append((tx, ty, n_cnt+1))

    return 0

arr = [list(input()) for _ in range(8)]

all_arr = []
all_arr.append(arr)
# print(arr)
# print(all_arr)

for i in range(6, -1, -1):
    # # tmp = [item[:] for item in arr]
    # tmp = arr.pop()
    # if '#' in tmp:
    #     arr.insert(0, ['.', '.', '.', '.', '.', '.', '.', '.'])
    # else:
    #     arr.insert(0, tmp)
    # arr.append(arr.pop())
    # tmp_arr = [item[:] for item in arr]
    tmp_arr = []
    for j in range(7-i):
        tmp_arr.append(['.', '.', '.', '.', '.', '.', '.', '.'])
    for j in range(i+1):
        tmp_arr.append(arr[j])
    all_arr.append(tmp_arr)


    # pprint.pprint(arr)
    # all_arr.append(tmp_arr)
# pprint.pprint(all_arr)
flag = False
print(bfs(7, 0, 0))