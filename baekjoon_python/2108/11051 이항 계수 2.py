
def binomial_coefficient(n, k):
    # 1.
    cache = [[0 for _ in range(k+1)] for _ in range(n+1)]

    # (n, k) = (n-1, k) + (n-1, k-1)
    # 2.
    for i in range(n+1):
        cache[i][0] = 1
    for i in range(k+1):
        cache[i][i] = 1

    # 3.
    for i in range(1, n+1):
        for j in range(1, k+1):
            cache[i][j] = (cache[i-1][j] + cache[i-1][j-1]) % 10007

    return cache[n][k]


n, k = map(int, input().split())
print(binomial_coefficient(n, k))
