

def dfs(idx, sum_value):
    global ans
    if sum_value >= ans:
        return
    if idx == n:
        ans = sum_value
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            dfs(idx + 1, sum_value + arr[idx][i])
            visited[i] = 0


for t in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    ans = 100000
    dfs(0, 0)
    print('#{} {}'.format(t+1, ans))


