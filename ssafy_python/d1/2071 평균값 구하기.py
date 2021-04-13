T = int(input())

for t in range(T):
    arr = list(map(int, input().split()))
    result = 0
    sums = 0
    for i in arr:
        sums += i
    # round 해당 값을 해당 자릿수에서 반올림(0은 소수 첫째자리)
    result = int(round(sums / len(arr), 0))

    print(f'#{t+1} {result}')