n = int(input())
ls = list(map(int, input().split()))

for i, v in enumerate(ls):
    for j in range(i+1, len(ls)):
        if ls[i] > ls[j]:
            ls[i], ls[j] = ls[j], ls[i]

print(ls[n//2])