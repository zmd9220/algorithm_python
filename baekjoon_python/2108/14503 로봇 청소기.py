import pprint
# 북, 동, 남, 서 기준 왼쪽은 0, 1, 2, 3
# 북, 동, 남, 서
# delta = [[(0, -1), (1, 0), (0, 1), (-1, 0)],
#          [(-1, 0), (0, 1), (1, 0), (0, -1)],
#          [(0, 1), (-1, 0), (0, -1), (1, 0)],
#          [(1, 0), (0, 1), (-1, 0), (0, -1)]
#          ]

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def dfs():
    st = [(r, c, d)]
    cnt = 0
    while st:
        nx, ny, nd = st.pop()
        if not arr[nx][ny]:
            arr[nx][ny] = 2
            cnt += 1
        flag = True
        now_delta = nd
        for i in range(4):
            now_delta = now_delta - 1
            if now_delta < 0:
                now_delta = 3
            # tx, ty = nx + delta[nd][i][0], ny + delta[nd][i][1]
            tx, ty = nx + delta[now_delta][0], ny + delta[now_delta][1]
            if 0 <= tx < n and 0 <= ty < m and not arr[tx][ty]:
                st.append((tx, ty, now_delta))
                flag = False
                break
        # back_delta = nd - 1
        # if back_delta < 0:
        #     back_delta = 3
        # if flag and arr[nx+delta[back_delta][0]][ny+delta[back_delta][1]] == 2:
        #     st.append((nx+delta[back_delta][0], ny+delta[back_delta][1], nd))
        # elif flag and arr[nx+delta[back_delta][0]][ny+delta[back_delta][1]] == 1:
        #     break
        if flag and arr[nx-delta[nd][0]][ny-delta[nd][1]] == 2:
            st.append((nx-delta[nd][0], ny-delta[nd][1], nd))
        elif flag and arr[nx-delta[nd][0]][ny-delta[nd][1]] == 1:
            break
        # if flag and arr[nx+delta[nd][back_delta][0]][ny+delta[nd][back_delta][1]] == 2:
        #     st.append((nx+delta[nd][back_delta][0], ny+delta[nd][back_delta][1], nd))
        # elif flag and arr[nx+delta[nd][back_delta][0]][ny+delta[nd][back_delta][1]] == 1:
        #     break
    return cnt

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

print(dfs())

pprint.pprint(arr)