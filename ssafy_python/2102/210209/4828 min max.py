t = int(input())
for T in range(t):
    N = int(input())
    arr = list(map(int, input().split()))
    min_n = arr[0]
    max_n = arr[0]
    for i in arr:
        if min_n > i:
            min_n = i
        if max_n < i:
            max_n = i
    print(f'#{T+1} {max_n - min_n}')