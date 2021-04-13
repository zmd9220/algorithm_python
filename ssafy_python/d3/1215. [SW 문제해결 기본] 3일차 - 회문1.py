for t in range(1, 11):
    n = int(input())
    arr = [input() for _ in range(8)]
    vertical_arr = []
    for i in range(8):
        vertical_arr_tmp = ''
        for j in range(8):
            vertical_arr_tmp += arr[j][i]
        vertical_arr.append(vertical_arr_tmp)
    # print(arr)
    # print(vertical_arr)
    cnt = 0
    for i in range(8):
        for j in range(8):
            # 가로
            # 배열 범위 초과 확인
            # j부터 j+n 전까지 이므로 8까지 커버 가능 **
            if j+n <= 8:
                string = arr[i][j:j+n]
                palindrome = string[::-1]
                if string == palindrome:
                    # print('가로', string, palindrome)
                    cnt += 1

                # print()
                string2 = vertical_arr[i][j:j + n]
                palindrome2 = string2[::-1]
                if string2 == palindrome2:
                    # print(string2, palindrome2)
                    cnt += 1
    print('#{} {}'.format(t, cnt))