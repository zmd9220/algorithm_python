
def is_sosu(num):
    dp = [1] * (num + 1)
    for i in range(2, num+1):
        if dp[i]:
            for j in range(i+i, num+1, i):
                dp[j] = 0
    for i in range(1, num+1):
        if dp[i]:
            print(i, end=' ')

is_sosu(500)