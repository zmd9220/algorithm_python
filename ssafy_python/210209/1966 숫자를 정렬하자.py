T = int(input())
# 배운 정렬 1. 버블 정렬 2. 카운팅 정렬
# 여기서 카운팅 정렬을 하면 테스트케이스에 1, 1, 1, 3, 1000000000 이 될경우 문제가 됨(그럴일은 적겠지만)
# 위의 경우는 불가능 한건 아닌데 시간이 길어질것 하지만 일반적인 케이스 길이50짜리에 최대 숫자가 50정도라면 훨씬 빠를 것(n+k시간)
# 여기서는 특수한 경우를 위해 버블정렬로 구현
for t in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(len(arr)-1, -1, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    # 출력부
    print(f'#{t+1}', end=' ')
    for i in arr:
        print(i, end=' ')
    print()

    # 내가 주로 쓰는것
    # for i in range(len(arr)):
    #     for j in range(i, len(arr)):
    #         if arr[i] > arr[j]:
    #            arr[i], arr[j] = arr[j], arr[i]
