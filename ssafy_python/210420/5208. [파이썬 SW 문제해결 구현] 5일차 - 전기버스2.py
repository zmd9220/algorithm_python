
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
