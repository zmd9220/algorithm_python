
for t in range(int(input())):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    w = [0] * n
    b = [0] * n
    r = [0] * n

    for i in range(n):
        for j in range(m):
            if arr[i][j] != 'W':
                w[i] += 1
            if arr[i][j] != 'B':
                b[i] += 1
            if arr[i][j] != 'R':
                r[i] += 1

    for i in range(1, n):
        w[i] += w[i-1]
        b[i] += b[i-1]
        r[i] += r[i-1]

    ans = 999999999

    for i in range(n-2):
        for j in range(i+1, n-1):
            w_cnt = w[i]
            b_cnt = b[j] - b[i]
            r_cnt = r[n-1] - r[j]

            if ans > w_cnt+b_cnt+r_cnt:
                ans = w_cnt+b_cnt+r_cnt
    print('#{} {}'.format(t+1, ans))