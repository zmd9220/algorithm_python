
# arr = []
#
# cnt = 1
# for i in range(5):
#     ls = []
#     for j in range(5):
#         ls.append(cnt)
#         cnt += 1
#     arr.append(ls)

arr=[[1, 4, 5, 9, 3], [4, 5, 2, 8, 9], [8, 5, 7, 3, 4], [9, 4, 1, 6, 3], [6, 5, 7, 2, 9]]

lr = [-1, 1, 0, 0]
td = [0, 0, -1, 1]
# 12345
# 678910 이런식으로 배열이 정리되어있으므로
# i는 y축 j는 x축 [i][j]

# y축
for i in range(len(arr)):
    # x축
    for j in range(len(arr[i])):
        result = 0
        for c in range(4):
            # x축 좌표 이동
            x = j + lr[c]
            # y축 좌표 이동
            y = i + td[c]
            # 좌표 이동으로 -1이 되거나 현재 배열기준 x, y가 5가 된경우(배열의 좌표 범위 초과) 무시
            if x < 0 or y < 0 or x == len(arr[i]) or y == len(arr):
                continue
            tmp = arr[i][j] - arr[y][x]
            # abs 써도 무방
            if tmp < 0:
                tmp = -tmp
            result += tmp
        print(f'result arr y={i} x={j} {result}')



