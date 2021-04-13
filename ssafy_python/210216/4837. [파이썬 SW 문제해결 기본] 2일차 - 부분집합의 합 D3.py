# 전체의 부분집합을 구하되(12) 해당 부분집합의 길이가(배열의 길이, len(sub)) n과 같고 해당 부분집합의 합(SUM)이 k와 같을 때만 카운트
for t in range(int(input())):
    n, k = map(int, input().split())
    cnt = 0
    arr = [i for i in range(1, 13)]
    arr2 = []
    for i in range(1 << 12):
        SUM = 0
        sub = []
        for j in range(12):
            if i & (1 << j):
                SUM += arr[j]
                sub.append(arr[j])
        # print(sub)

        if SUM == k and len(sub) == n:
            cnt += 1
            # print(sub)
    print(f'#{t+1} {cnt}')
