
delta = [[0, 1], [0, -1], [1, 1], [1, 0], [1, -1], [-1, 1], [-1, 0], [-1, -1]]


def gomoku(arr, x, y, delta_x, delta_y):

    tmp_x = x+delta_x
    tmp_y = y+delta_y
    cnt = 1
    while True:
        if not 0 <= tmp_x < len(arr) or not 0 <= tmp_y < len(arr):
            return False
        if arr[tmp_x][tmp_y] != 'o':
            return False
        tmp_x += delta_x
        tmp_y += delta_y
        cnt += 1
        if cnt >= 5:
            return True


for t in range(int(input())):
    arr = []
    n = int(input())
    flag = False
    for _ in range(n):
        arr.append(input())
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'o':
                for k in range(len(delta)):
                    if gomoku(arr, i, j, delta[k][0], delta[k][1]):
                        flag = True
                        break
            if flag:
                break
        if flag:
            break
    print('#{} {}'.format(t+1, 'YES' if flag else 'NO'))

