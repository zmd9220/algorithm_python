def binarysearch(l, r, cnt, page):
    c = int((l + r) / 2)
    if c == page:
        return cnt
    elif c > page:
        return binarysearch(l, c, cnt + 1, page)
    else:
        return binarysearch(c, r, cnt + 1, page)


for t in range(int(input())):
    p, a, b = map(int, input().split())
    cntA = binarysearch(1, p, 1, a)
    cntB = binarysearch(1, p, 1, b)
    result = ''
    if cntA == cntB:
        result = '0'
    elif cntA > cntB:
        result = 'B'
    else:
        result = 'A'
    print(f'#{t + 1} {result}')
