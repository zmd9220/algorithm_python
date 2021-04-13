# 홀수는 오름차순, 짝수는 내림차순으로 정렬하기 여기선 버블이 어렵고 셀렉션 정렬을 이용해야함
for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n-1):
        # 나머지가 1인 경우 = 홀수, 오름차순
        if i % 2:
            # min_idx, max_idx 의 시작 주소는 i부터(앞은 정렬되어 있으므로)
            min_idx = i
            for j in range(i+1, n):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        # 짝수인 경우 0, 2, 4, 6 ...
        else:
            max_idx = i
            for j in range(i+1, n):
                if arr[max_idx] < arr[j]:
                    max_idx = j
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
    # 출력부
    print(f'#{t+1} ', end='')
    for i in range(10):
        print(arr[i], end=' ')
    print()
