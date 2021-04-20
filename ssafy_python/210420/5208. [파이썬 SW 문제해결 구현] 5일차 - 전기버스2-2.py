
for t in range(int(input())):
    arr = list(map(int, input().split()))
    n = arr.pop(0)
    ans = [-1] * n
    for i in range(n-1):
        for j in range(1, arr[i]+1):
            if i+j >= n:
                break
            if ans[i+j] == -1:
                ans[i+j] = ans[i] + 1
            else:
                ans[i+j] = min(ans[i]+1, ans[i+j])
            # print(ans)
    print('#{} {}'.format(t+1, ans[n-1]))


# D3 5208 전기버스2
def dfs(idx, _sum):
    global answer
    if answer < _sum: return
    if idx >= N:
        answer = _sum
        return
    count = station[idx]
    for i in range(count, 0, -1):
        dfs(idx + i, _sum + 1)


for t in range(int(input())):
    answer = float('inf')
    station = list(map(int, input().split()))
    # 0부터 시작하니까 -1
    N = station.pop(0) - 1
    # 처음 충전은 안치니까 -1로 시작해서 보정해주기
    dfs(0, -1)
    print('#{} {}'.format(t + 1, answer))