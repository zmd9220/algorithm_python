T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    case = len(a) - len(b)
    max_n = 0
    # case가 0보다 크면 a가 b보다 길이가 기므로 b를 고정하고 a의 인덱스를 움직이며 곱셈
    if case > 0:
        # 전체 경우의 수는 둘의 길이 차이 +1
        case += 1
        for i in range(case):
            sum = 0
            for j in range(len(b)):
                sum += b[j] * a[j+i]
            if sum > max_n:
                max_n = sum
    # case가 0보다 작으면 a를 고정하고 b를 움직이며 곱셈 그리고 case를 음수에서 양수로 체인지
    else:
        case = -case + 1
        for i in range(case):
            sum = 0
            for j in range(len(a)):
                sum += a[j] * b[j+i]
            if sum > max_n:
                max_n = sum
    print(f'#{t+1} {max_n}')