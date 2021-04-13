for t in range(10):
    arr = []
    n = int(input())
    for i in range(100):
        arr.append(list(map(int, input().split())))

    ran = len(arr)
    result = 0
    # max_row = 0
    # max_col = 0
    max_dia = 0
    max_dia2 = 0
    # 행 우선 탐색
    for i in range(ran):
        tmp = 0
        for j in range(ran):
            tmp += arr[i][j]
        # if tmp > max_row:
        #     max_row = tmp
        if tmp > result:
            result = tmp

    # 열 우선 탐색
    for i in range(ran):
        tmp = 0
        for j in range(ran):
            tmp += arr[j][i]
        # if tmp > max_col:
        #     max_col = tmp
        if tmp > result:
            result = tmp

    # 오른쪽 아래 대각선
    for i in range(ran):
        max_dia += arr[i][i]
    if max_dia > result:
        result = max_dia

    # 왼쪽 아래 대각선
    for i in range(ran-1, -1, -1):
        max_dia2 += arr[ran-1-i][i]
    if max_dia2 > result:
        result = max_dia2

    print(f'#{n} {result}')
    # print(n)
    # print(max_row, max_col, max_dia, max_dia2)
    # print(max(max_row, max_col, max_dia, max_dia2))


