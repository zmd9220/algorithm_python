T = int(input())
for t in range(T):
    n, q = map(int, input().split())
    # l,r은 최대 n을 넘지 않으므로 n 크기의 배열 생성
    arr = [0] * n
    for i in range(1, q+1):
        l, r = map(int, input().split())
        # 0번 인덱스 부터 n-1까지의 배열이므로 l-1 ~ r 앞까지
        for j in range(l-1, r):
            # 해당 범위의 값을 전체 i(현재 i번째 작업이므로)로 변경
            arr[j] = i
    # 출력부
    print(f'#{t+1}', end=' ')
    for i in arr:
        print(i, end=' ')
    print()