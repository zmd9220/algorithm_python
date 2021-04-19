
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for t in range(int(input())):
    arr = [list(input().split()) for _ in range(4)]
    ans = set()
    for i in range(4):
        for j in range(4):
            q = [[i, j, 1, arr[i][j]]]
            while len(q):
                x, y, cnt, string = q.pop(0)
                if cnt == 7:
                    ans.add(string)
                    continue
                for k in range(len(dr)):
                    new_x, new_y = x+dr[k], y+dc[k]
                    if 0 <= new_x < 4 and 0 <= new_y < 4:
                        q.append([new_x, new_y, cnt+1, string+arr[new_x][new_y]])
    print('#{} {}'.format(t+1, len(ans)))
    # print(ans)
    # print(len(ans))