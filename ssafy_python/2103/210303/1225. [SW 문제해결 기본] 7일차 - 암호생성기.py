for t in range(1, 11):
    tc = int(input())
    arr = list(map(int, input().split()))
    # 빼기를 했을때 0이하가 발생하는 순간 프로그램 종료를 위해
    flag = False
    while not flag:
        # 1~5까지 빼주는 사이클
        for i in range(1, 6):
            arr[0] -= i
            # dequeue
            tmp = arr.pop(0)
            # enqueue
            arr.append(tmp)
            # 탈출조건 빼기한 결과가 0이하
            if arr[-1] <= 0:
                arr[-1] = 0
                flag = True
                break
    print('#{} {}'.format(tc, ' '.join(map(str, arr))))
