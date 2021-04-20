# def permutation(arr, r):
#     # 1.
#     arr = sorted(arr)
#     used = [0 for _ in range(len(arr))]
#     result = []
#
#     def generate(chosen, used):
#         # 2.
#         if len(chosen) == r:
#             # result.append(chosen)
#             # print(chosen)
#             # print(''.join(map(str, chosen)))
#             result.append(''.join(map(str, chosen)))
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
#     return result


# def min_value(data, d_size, perm):
#     result = 100000
#     for i in range(len(perm)):
#         tmp_value = 0
#         for j in range(d_size):
#             # print(int(perm[i][j]))
#             # print(arr[j][int(perm[i][j])])
#             tmp_value += arr[j][int(perm[i][j])]
#             if result <= tmp_value:
#                 break
#         if result > tmp_value:
#             result = tmp_value
#     return result

def dfs(idx, _sum):
    global answer
    if _sum >= answer:
        return
    if idx == N:
        answer = _sum
    for i in range(N):
        if visited[i]:
            visited[i] = 0
            dfs(idx + 1, _sum + V[idx][i])
            visited[i] = 1


for t in range(int(input())):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    visited = [1 for _ in range(N)]
    answer = 999999
    dfs(0, 0)
    print('#{} {}'.format(t + 1, answer))


for t in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    p_arr = list(range(n))
    perms = permutation(p_arr, n)
    # print(perms)
    ans = min_value(arr, n, perms)
    print('#{} {}'.format(t+1, ans))

# ans = permutation('ABCD', 4)
#
# print(ans)
