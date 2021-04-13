for t in range(int(input())):
    d, l, n = map(int, input().split())
    damage = 0
    for i in range(n):
        damage += d * (1 + (i * l / 100))
    da = n * d + (d * n * (n-1) * l / 200)
    # print(int(da))
    print('#{} {}'.format(t + 1, int(damage)))
