# def permutation(arr, r):
#     # 1.
#     # arr = sorted(arr)
#     used = [0 for _ in range(len(arr))]
#
#     def generate(chosen, used):
#         # 2.
#         if len(chosen) == r:
#             # print(chosen)
#             perm_list.append(chosen)
#             return
#
#         # 3.
#         for i in range(len(arr)):
#             if not used[i]:
#                 chosen.append(arr[i])
#                 used[i] = 1
#                 generate(chosen, used)
#                 used[i] = 0
#                 chosen.pop()
#
#     generate([], used)

from itertools import permutations

for t in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # for i in range(1, n):
    perm = [i for i in range(1, n)]
    perm_list = list(permutations(perm, n-1))
    # print(perm)
    # permutation(perm, len(perm))
    # print(perm_list)
    sums = []
    for i in range(len(perm_list)):
        arr_sum = 0
        for j in range(n):
            # 시작점 0 인덱스 끝점 0인덱스 제외
            # arr[perm_list[i][j-1]][perm_list[i][j]]
            # (1, 2), (2, 1)
            # e[0][1] + e[1][2] + e[2][0]
            # e[0][2] + e[2][1] + e[1][0]
            if j == 0:
                arr_sum += arr[0][perm_list[i][j]]
            elif j+1 >= n:
                arr_sum += arr[perm_list[i][j-1]][0]
            else:
                arr_sum += arr[perm_list[i][j-1]][perm_list[i][j]]
        # print(arr_sum)
        sums.append(arr_sum)
    print('#{} {}'.format(t+1, min(sums)))
