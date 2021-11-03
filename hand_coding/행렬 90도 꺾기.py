
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
tmp = [[0] * len(lst) for _ in range(len(lst))]

for x in range(len(lst)):
    for y in range(len(lst)):
        # 오답
        # tmp[y][x] = lst[len(lst)-x-1][y]
        # 정답
        tmp[y][len(lst)-x-1] = lst[x][y]
print(tmp)