for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    length = len(arr)
    # 셀렉션
    for i in range(length-1):
        min_idx = i
        for j in range(i+1, length):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    # 버블
    # for i in range(length-1, -1, -1):
    #     # for j in range(i-1, -1, -1):
    #     #     if arr[j] > arr[i]:
    #     #         arr[j], arr[i] = arr[i], arr[j]
    #     for j in range(i):
    #         if arr[j] > arr[j+1]:
    #             arr[j], arr[j+1] = arr[j+1], arr[j]
    result = " ".join(map(str, arr))
    print(f'#{t+1} {result}')