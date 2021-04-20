import sys

sys.stdin = open('input (1).txt', 'r')

def dfs(idx, mul_value):
    global ans
    if mul_value <= ans:
        return
    if idx == n:
        ans = mul_value
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            dfs(idx + 1, mul_value * (arr[idx][i]/100))
            visited[i] = 0


for t in range(int(input())):
    n = int(input())
    arr = [list(map(float, input().split())) for _ in range(n)]
    visited = [0] * n
    ans = -50.0
    dfs(0, 1.0)
    print('#{} {:.6f}'.format(t+1, (ans*100)))