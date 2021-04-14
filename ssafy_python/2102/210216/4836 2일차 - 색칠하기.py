# 입력부
# 1, 2로 주어진 공간을 칠하기 이미 누가 색칠했으면 패스, 3일 경우도 패스
for t in range(int(input())):
    arr = [[0]*10 for i in range(10)]
    cnt = 0
    for n in range(int(input())):
        colors = list(map(int, input().split()))

        # 색칠하기 뒤의 +1은 입력 받은 좌표 전까지 이므로 +1 해줘야함
        for x in range(colors[0], colors[2]+1):
            for y in range(colors[1], colors[3]+1):
                # 이미 같은 색으로 칠했을 경우 패스, 이미 겹친 색으로 칠했을 경우(3) 패스
                if arr[x][y] == colors[4] or arr[x][y] == 3:
                    continue
                arr[x][y] += colors[4]
    # 순회하며 3인 공간 찾기
    for x in range(len(arr)):
        for y in range(len(arr)):
            if arr[x][y] == 3:
                cnt += 1
    print(f'#{t+1} {cnt}')
