n = int(input())

for t in range(n):
    ls = list(map(int, input().split()))

    for i, v in enumerate(ls):
        for j in range(i+1, len(ls)):
            if ls[i] > ls[j]:
                ls[i], ls[j] = ls[j], ls[i]

    print(f'#{t+1} {ls[-1]}')