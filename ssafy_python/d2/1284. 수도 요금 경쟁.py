T = int(input())

for t in range(T):
    p, q, r, s, w = map(int, input().split())
    result = p * w
    b = q
    if w-r > 0:
        b += s * (w-r)
    if result > b:
        result = b

    print(f'#{t+1} {result}')

