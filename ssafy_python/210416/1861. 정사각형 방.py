
# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]
#
#
# def bfs(data, d_size):
#     cnt = -1
#     cnt_start_value = 100000
#     q = []
#     for i in range(d_size):
#         for j in range(d_size):
#             val = data[i][j]
#             now_cnt = 1
#             q.append([i, j])
#             while len(q):
#                 x, y = q.pop(0)
#                 for k in range(len(dr)):
#                     new_x, new_y = x+dr[k], y+dc[k]
#                     # 4방향 중 자신+1 크기의 방을 찾으면 바로 건너뛰기 (bfs에서 조금 변형)
#                     if new_x < d_size and new_x >= 0 and new_y < d_size and new_y >= 0:
#                         if val+1 == data[new_x][new_y]:
#                             q.append([new_x, new_y])
#                             now_cnt += 1
#                             val += 1
#                             break
#             if now_cnt > cnt:
#                 cnt = now_cnt
#                 cnt_start_value = data[i][j]
#             elif now_cnt == cnt:
#                 if cnt_start_value > data[i][j]:
#                     cnt_start_value = data[i][j]
#     return cnt_start_value, cnt
#
#
# for t in range(int(input())):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     ans, cnt = bfs(arr, n)
#     print('#{} {} {}'.format(t+1, ans, cnt))


for t in range(1, int(input()) + 1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    # UDLR
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    cnt = [0] * (N * N + 1)

    for i in range(N):
        for j in range(N):
            val = rooms[i][j]
            for idx in range(4):
                r, c = i + dr[idx], j + dc[idx]
                if 0 <= r < N and 0 <= c < N and rooms[r][c] == val + 1:
                    cnt[rooms[i][j]] = 1
                    break
    print(cnt)
    for i in range(N * N, 0, -1):
        if cnt[i]:
            cnt[i] = cnt[i + 1] + 1
        else:
            cnt[i] = 1
    print(cnt)
    max_move = max(cnt)
    idx = cnt.index(max_move)
    print('#{} {} {}'.format(t, idx, max_move))