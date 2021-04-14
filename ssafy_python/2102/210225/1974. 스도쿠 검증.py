# 가로 검증, 세로 검증, 3*3 검증 3가지를 나눠서 진행
def is_sudoku(lists):
    # 현 문제에선 모두 가로 세로 9*9 고정이므로 범위를 9로잡음
    # 검증은 0~8 인덱스의 합이 1~9까지의 합 = 45인 경우만 옳다. 9*10/2 = 45
    # 가로 검증
    for i in range(9):
        check = 0
        for j in range(9):
            check += lists[i][j]
        if check != 45:
            # print('가로', check)
            return 0
    # 세로 검증
    for i in range(9):
        check = 0
        for j in range(9):
            check += lists[j][i]
        if check != 45:
            # print('세로', check)
            return 0
    # 3*3 검증
    for i in range(0, 9, 3):
        check = 0
        for j in range(i, i+3):
            for k in range(i, i+3):
                check += lists[j][k]
        if check != 45:
            # print('3*3', check)
            return 0
    # 모든 검증을 통과하면 1
    return 1


for t in range(int(input())):
    arr = [list(map(int, input().split())) for _ in range(9)]
    # print(arr)
    print('#{} {}'.format(t+1, is_sudoku(arr)))