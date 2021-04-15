# dfs, bfs, 순열 모두 가능?

# def bfs(data, d_size, ans_arr):
#     start = arr[0][0]
#     ans[0][0]

# 누적합 dp?
def dp(data, d_size):
    for i in range(d_size):
        for j in range(d_size):
            before_row = 10000
            before_col = 10000
            if i == 0 and j == 0:
                memo[i][j] = arr[i][j]
                continue
            if i-1 >= 0:
                before_row = memo[i - 1][j]
            if j-1 >= 0:
                before_col = memo[i][j - 1]
            memo[i][j] = arr[i][j] + min(before_col, before_row)
    return memo[d_size - 1][d_size - 1]


for t in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # perm = []
    memo = [[0] * n for _ in range(n)]
    ans = dp(arr, n)
    print('#{} {}'.format(t+1, ans))

