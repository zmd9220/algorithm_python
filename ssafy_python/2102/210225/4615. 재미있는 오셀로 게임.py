# def chk_color(arr, x, y):
#     direction = [[-1, 1], [-1, 0], [-1, -1], [0, 1], [0, -1], [1, 1], [1, 0], [1, -1]]


for t in range(int(input())):
    n, m = map(int, input().split())
    arr = [[0] * (n+1) for _ in range(n+1)]
    direction = [[-1, 1], [-1, 0], [-1, -1], [0, 1], [0, -1], [1, 1], [1, 0], [1, -1]]
    # 가운데 지점 세팅하기
    mid = n//2
    # 백 흑
    # 흑 백
    arr[mid][mid] = 2
    arr[mid+1][mid+1] = 2
    arr[mid][mid+1] = 1
    arr[mid+1][mid] = 1

    for i in range(m):
        x, y, bw = map(int, input().split()) # 좌표 및 흑돌, 백돌 선택
        arr[x][y] = bw


        # 반대 색 구하기
        if bw == 1:
            rev = 2
        else:
            rev = 1
        # 일단 삽입 후 가로 세로 대각선 변동여부 확인
        # 뒤집는 조건은 해당하는 곳에 반대색 돌이 있고 끝에 같은색의 돌이 있을 경우
        for j in direction:
            tmp_x, tmp_y = x + j[0], y + j[1]
            change = []
            # # 바로 옆 돌이 같은 색이 아니고 0이 아닌경우(아무것도 없는 곳이 아님) = 다른 돌이 있을 경우
            # if arr[tmp_x][tmp_y] == rev:
            # 해당 방향으로 끝까지 탐색 (같은 돌을 만나기 전까지)
            while True:
                # 범위 나감
                if tmp_x <= 0 or tmp_y <= 0 or tmp_x > n or tmp_y > n:
                    change = []
                    break
                # 범위 내에서 같은 돌을 찾아냄
                elif arr[tmp_x][tmp_y] == bw:
                    break
                # 범위 내에서 다른 돌을 찾아냄
                elif arr[tmp_x][tmp_y] == rev:
                    change.append([tmp_x, tmp_y])
                # 그외의 경우는 0일 때
                else:
                    change = []
                    break
                tmp_x += j[0]
                tmp_y += j[1]
            # 해당 하는 다른 색 돌 변경
            for k in change:
                arr[k[0]][k[1]] = bw

    # 검은 돌 흰 돌 갯수 구하기
    black, white = 0, 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if arr[i][j] == 1:
                black += 1
            elif arr[i][j] == 2:
                white += 1

    print('#{} {} {}'.format(t+1, black, white))