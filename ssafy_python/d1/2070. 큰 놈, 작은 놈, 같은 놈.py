T = int(input())

for t in range(T):
    a, b = map(int, input().split())
    if a > b:
        result = '>'
    elif a < b:
        result = '<'
    else:
        result = '='

    print(f'#{t+1} {result}')