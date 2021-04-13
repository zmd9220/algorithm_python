T = int(input())

for t in range(T):
    n = int(input())
    # 소인수 분해 요소 a,b,c,d,e
    ls = [2, 3, 5, 7, 11]
    answer = [0] * 5
    idx = 4 # e = 11 부터 소인수분해 진행할 것
    while idx > -1:
        if n % ls[idx] == 0:
            answer[idx] += 1
            n /= ls[idx]
        else:
            idx -= 1

    print(f'#{t+1}', end=' ')
    for i in answer:
        print(i, end=' ')
    print()