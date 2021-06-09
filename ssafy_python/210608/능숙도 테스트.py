
str = 'ASADADAS'

# 1번
# max_cnt = 0
# max_char = ''
# arr1 = {}
# for i in range(len(str)):
#     if str[i] not in arr1:
#         arr1[str[i]] = 0
#     else:
#         arr1[str[i]] += 1
#
# for i, j in arr1.items():
#     if j > max_cnt:
#         max_cnt = j
#         max_char = i
# print(max_char, max_cnt)

def func(a, idx):
    print(a[idx], end='')
    if idx == len(a) - 1:
        print()
    else:
        func(a, idx+1)
    print(a[idx], end='')

func(str, 0)


# 2번
# str2 = 'SSADADAAASADAAAS'

#
# ans = {}
# n = 5
#
# tmp = str2[:n]
# print(tmp)
# for i in range(n, len(str2)):
#     tmp_max_cnt = 0
#     tmp_max_char = ''
#     arr2 = {}
#     for j in range(len(tmp)):
#         if tmp[j] not in arr2:
#             arr2[tmp[j]] = 1
#         else:
#             arr2[tmp[j]] += 1
#         print(arr2)
#     for k, j in arr2.items():
#         if j > tmp_max_cnt:
#             tmp_max_cnt = j
#             tmp_max_char = k
#     if tmp_max_char not in ans:
#         ans[tmp_max_char] = 1
#     else:
#         ans[tmp_max_char] += 1
#     tmp = tmp[1:] + str2[i]
# print(ans)
# max_cnt = 0
# max_char = ''
# for i, j in ans.items():
#     if j > max_cnt:
#         max_cnt = j
#         max_char = i
#
# print(max_char, max_cnt)


