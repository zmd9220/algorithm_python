# 풀었던 문제 다시풀기
for t in range(int(input())):
    n, q = map(int, input().split())
    arr = [0] * n
    # i는 현재 붙일 번호
    for i in range(1, q+1):
        l, r = map(int, input().split())
        # 인덱스 시작은 0번이고 ~n-1까지가 인덱스 범위 이므로 시작 위치 조정
        # 끝나는 범위도 파이썬에선 해당 번호 전까지이므로 +1이겠지만 인덱스 번호 조정으로 -1 즉 0
        for j in range(l-1, r):
            arr[j] = i
    print('#{} {}'.format(t+1, ' '.join(map(str, arr))))