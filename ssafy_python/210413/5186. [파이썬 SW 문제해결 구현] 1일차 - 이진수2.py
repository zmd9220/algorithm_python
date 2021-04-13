
for t in range(int(input())):
    # print(1 * (2**-1))
    n = float(input())
    ans = ''
    while n != 0:
        n = n * 2
        if n >= 1:
            ans += '1'
            n -= 1
        else:
            ans += '0'
        if len(ans) >= 13:
            ans = 'overflow'
            break

    print('#{} {}'.format(t+1, ans))


