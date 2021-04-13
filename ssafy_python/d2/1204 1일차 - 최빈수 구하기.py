T = int(input())

for t in range(T):
    # 점수 카운팅 배열
    arr = [0] * 101
    n = int(input())
    scores = list(map(int, input().split()))
    max_v = 0
    result = 0
    # 점수를 카운터 배열에 넣어 카운트하기
    for i in scores:
        arr[i] += 1
    for i in range(1, len(arr)):
        if arr[i] >= max_v:
            max_v = arr[i]
            result = i

    print(f'#{n} {result}')
