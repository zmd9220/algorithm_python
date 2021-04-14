# 전체 순회 시작해서 흰색인 곳 찾으면 거기에서 부터 상하좌우 탐색,
# 해당 상하좌우 끝까지 돌았을 때 단어의 길이(k)와 같으면 카운트 +1

# 다시 보니 상하좌우가 아닌 좌->우 방향 or 위->아래만 체크하면 됨
# 좌우, 위아래 체크를 같이하면 처리가 힘드므로 가로 세로 따로따로 계산
# 동시에 시작점은 나보다 앞에 값이 없어야 하므로 0번 인덱스 또는 내 앞 인덱스 값이 0일때만 시행가능

for t in range(int(input())):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    # 가로 검사
    for i in range(n):
        for j in range(n):
            # 현재 자리가 1이고 현재 내가 0번 인덱스 거나 앞의 인덱스가 0 = 즉 내가 첫번째 시작일 때
            if arr[i][j] == 1 and (j == 0 or arr[i][j-1] == 0):
                # 좌 -> 우
                x, y = i, j
                cnt = 1
                while y < n-1 and arr[x][y+1] == 1:
                    cnt += 1
                    y += 1
                if cnt == k:
                    result += 1

    # 세로 검사
    for i in range(n):
        for j in range(n):
            # 현재 자리가 1이고 현재 내가 0번 인덱스 거나 앞의 인덱스가 0 = 즉 내가 첫번째 시작일 때
            if arr[j][i] == 1 and (j == 0 or arr[j-1][i] == 0):
                # 위 -> 아래
                x, y = j, i
                cnt = 1
                while x < n-1 and arr[x+1][y] == 1:
                    cnt += 1
                    x += 1
                if cnt == k:
                    result += 1
    print(f'#{t + 1} {result}')

            # if arr[i][j] == 1:
            #     # 위->아래
            #     # x, y = i, j
            #     # cnt = 0
            #     # while x > 0 and arr[x-1][y] == 1:
            #     #     cnt += 1
            #     # if cnt == k:
            #     #     result += 1
            #
            #     x, y = i, j
            #     cnt = 1
            #     while x < n-1 and arr[x+1][y] == 1:
            #         cnt += 1
            #         x += 1
            #     if cnt == k:
            #         result += 1
            #
            #     # cnt = 0
            #     # while y > 0 and arr[x][y-1] == 1:
            #     #     cnt += 1
            #     # if cnt == k:
            #     #     result += 1
            #
            #     # 좌 -> 우
            #     x, y = i, j
            #     cnt = 1
            #     while y < n-1 and arr[x][y+1] == 1:
            #         cnt += 1
            #         y += 1
            #     if cnt == k:
            #         result += 1
    # print(f'#{t+1} {result}')