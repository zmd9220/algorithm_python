#
# n = int(input())
# arr = list(map(int, input().split()))
# check = [0] * 10001
# factorials = [0] * 10001
# factorials[0] = 1
# for i in range(1, 10001):
#     factorials[i] = factorials[i-1] * i
#
# k_index = 1
# for i in range(n):
#     for j in range(1, arr[i]):
#         if not check[j]:
#             k_index += factorials[n-i-1]
#     check[arr[i]] = 1
#
# k_index += 1
#
# # print(k_index)
# if k_index == factorials[n]+1:
#     print(-1)
# else:
#     check = [0] * 10001
#     ans = []
#     for i in range(n):
#         for j in range(1, n+1):
#             if check[j]:
#                 continue
#             if factorials[n-i-1] < k_index:
#                 k_index -= factorials[n-i-1]
#             else:
#                 ans.append(j)
#                 check[j] = True
#                 break
#     for i in range(len(ans)):
#         print(ans[i], end=" ")

n = int(input())
arr = list(map(int, input().split()))

check_value = arr[-1]
for i in range(n-2, -1, -1):
    if check_value