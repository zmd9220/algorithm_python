
def chk():
    return 1

for t in range(int(input())):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        cnt = 0
        # 행을 검사
        for j in range(n):
            if arr[i][j] == 1:
                cnt += 1
            if arr[i][j] == 0 or j == n-1:
                # 벽을 만났을 때 그동안 쌓아온 cnt 값이 k이면 들어갈 수 있다.
                if cnt == k:
                    # print(j, j-1, j-2)
                    ans += 1
                cnt = 0
        # 열을 검사
        for j in range(n):
            if arr[j][i] == 1:
                cnt += 1
            if arr[j][i] == 0 or j == n-1:
                # 벽을 만났을 때 그동안 쌓아온 cnt 값이 k이면 들어갈 수 있다.
                if cnt == k:
                    # print(j, j-1, j-2)
                    ans += 1
                cnt = 0
    print('#{} {}'.format(t+1, ans))