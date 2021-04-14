# 이문제는 최단거리가 아니므로 bfs, dfs상관없이 구하기만 하면 됨

delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# bfs - 큐
def bfs(data):
    queue = []
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i][j] == 2:
                queue.append([i, j])
                break
    while len(queue):
        now_idx = queue.pop(0)
        for d in delta:
            x, y = now_idx[0] + d[0], now_idx[1] + d[1]
            # 범위 내이면서 0 = 통로
            if 0 <= x < len(data) and 0 <= y < len(data) and data[x][y] == 0:
                queue.append([x, y])
                data[x][y] = 1
            # 범위 내이면서 3 = 도착함
            elif 0 <= x < len(data) and 0 <= y < len(data) and data[x][y] == 3:
                return 1
    return 0

# dfs - 스택
def dfs(data):
    stack = []
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i][j] == 2:
                stack.append([i, j])
                break
    while len(stack):
        now_idx = stack.pop(-1)
        for d in delta:
            x, y = now_idx[0] + d[0], now_idx[1] + d[1]
            # 범위 내이면서 0 = 통로
            if 0 <= x < len(data) and 0 <= y < len(data) and data[x][y] == 0:
                stack.append([x, y])
                data[x][y] = 1
            # 범위 내이면서 3 = 도착함
            elif 0 <= x < len(data) and 0 <= y < len(data) and data[x][y] == 3:
                return 1
    return 0

for t in range(1, 11):
    tc = int(input())
    arr = []

    for _ in range(16):
        string = input()
        tmp = []
        for char in string:
            tmp.append(int(char))
        arr.append(tmp)
    # print(arr)
    print('#{} {}'.format(tc, dfs(arr)))
    # print('#{} {}'.format(tc, bfs(arr)))