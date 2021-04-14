# dfs, bfs 같은 탐색으로 최대 길이를 구해도 되고, for 문을 통해 가로세로를 구한뒤 그 범위만큼 0으로 체인지하는 방법도있음

def find_row_col(data, r, c):
    r_count = 0
    c_count = 0
    # 행 크기 찾기
    tmp = r
    while tmp< len(data) and data[tmp][c] != 0:
        r_count += 1
        tmp += 1
    tmp = c
    # 열 크기 찾기
    while  tmp < len(data) and data[r][tmp] != 0:
        c_count += 1
        tmp += 1
    # 해당 하는 범위 만큼 사각형 0으로 체인지
    for i in range(r_count):
        for j in range(c_count):
            data[r+i][c+j] = 0
    return r_count, c_count


for t in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = []
    # x,y 축을 탐색하며 가장 처음 0아닌 수를 만났을때 사각형 범위 찾는 함수실행
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                result.append(find_row_col(arr, i, j))
    # result 속의 행렬을 1.전체 크기 2.행 크기 순으로 정렬
    for i in range(len(result)-1):
        min_idx = i
        min_size = result[min_idx][0] * result[min_idx][1]
        for j in range(i+1, len(result)):
            j_size = result[j][0] * result[j][1]
            if min_size == j_size and result[min_idx][0] > result[j][0]:
                min_idx = j
            elif min_size > j_size:
                min_idx = j
                min_size = j_size
        result[min_idx], result[i] = result[i], result[min_idx]

    print('#{} {}'.format(t+1, len(result)), end=' ')
    for ch in result:
        print(ch[0], ch[1], end=' ')
    print()
    # print('#{} {} {}'.format(t+1, len(result), ' '.join(map(str, result[ch])) for ch in range(len(result))))
    #
    # print(i for i in range(5))
