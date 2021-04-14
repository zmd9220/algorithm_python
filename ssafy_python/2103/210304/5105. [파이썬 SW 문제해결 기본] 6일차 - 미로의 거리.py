# 미로같은 문제는 조건식을 짤때 편하게하기위해 가상의 벽을 하나더 치는방법과 그냥 조건식 그대로넣는방법 2개가있음
# 현 문제는 도착'거리'까지 고려하기때문에 bfs가 좀더 유효함
def bfs(data):
    queue = []
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    # 각각의 거리를 넣을 배열 생성 - 사실 딕셔너리로 해도됨
    distance = [[0] * len(data) for _ in range(len(data))]
    # 시작점 찾기
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i][j] == 2:
                # data[i][j] = 1
                queue.append([i, j])
                break
    while len(queue):
        now_idx = queue.pop(0)
        for direct in direction:
            x = now_idx[0] + direct[0]
            y = now_idx[1] + direct[1]
            # 좌표 변경값이 미로의 범위를 벗어나지 않았고, 해당 좌표의 값이 0이면(통로이면)
            if 0 <= x < len(data) and 0 <= y < len(data) and data[x][y] == 0:
                queue.append([x, y])
                # data[x][y] = data[now_idx[0]][now_idx[1]] + 1
                data[x][y] = 1
                distance[x][y] = distance[now_idx[0]][now_idx[1]] + 1
            # 좌표가 미로 범위 내이고, x,y가 도착지면(도착)
            elif 0 <= x < len(data) and 0 <= y < len(data) and data[x][y] == 3:
                # return data[now_idx[0]][now_idx[1]]
                return distance[now_idx[0]][now_idx[1]]
    return 0


for t in range(int(input())):
    n = int(input())
    arr = []
    for _ in range(n):
        tmp = input()
        val = []
        for char in tmp:
            val.append(int(char))
        arr.append(val)
    # print(arr)
    print('#{} {}'.format(t+1, bfs(arr)))