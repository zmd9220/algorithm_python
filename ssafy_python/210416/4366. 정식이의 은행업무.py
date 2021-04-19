

# for t in range(int(input())):
#     base2 = input()
#     base3 = input()
#     base2_val = 0
#     base3_val = 0
#     tmp_base2 = base2[::-1]
#     tmp_base3 = base3[::-1]
#     for i in range(len(base2)):
#         base2_val += int(tmp_base2[i])*(2**i)
#     for i in range(len(base3)):
#         base3_val += int(tmp_base3[i])*(3**i)
#
#     base2_arr = []
#     base3_arr = []
#     for i in range(len(base2)):
#         if base2[i] == '1':
#             base2_arr.append(base2_val - (2**(len(base2)-i)))
#         else:
#             base2_arr.append(base2_val + (2**(len(base2)-i)))
#
#     for i in range(len(base3)):
#             if base3[i] == '1':
#                 # base3_arr.append(base3_val - (3**(len(base3)-i)) + (3**(len(base3)-i))*2)
#                 # 2일 때
#                 base3_arr.append(base3_val + (3**(len(base3)-i)))
#                 # 0일 때
#                 base3_arr.append(base3_val - (3 ** (len(base3) - i)))
#             elif base3[i] == '0':
#                 # 1일 때
#                 base3_arr.append(base3_val + (3 ** (len(base3) - i)))
#                 # 2일 때
#                 base3_arr.append(base3_val + ((3 ** (len(base3) - i))*2))
#             else:
#                 # 0일 때
#                 base3_arr.append(base3_val - ((3 ** (len(base3) - i))*2))
#                 # 1일 때
#                 base3_arr.append(base3_val + (3 ** (len(base3) - i)))
#     print(base2_val, base2_arr)
#     print(base3_val, base3_arr)



for t in range(int(input())):
    base2 = input()
    base3 = input()
    base2_arr = []
    base3_arr = []
    base2_values = []
    base3_values = []
    # 가능한 모든 경우의 수를 구하는 과정
    for i in range(len(base2)):
        tmp = base2
        if tmp[i] == '1':
            # 그대로 넣기
            tmp = tmp[:i]+'0'+tmp[i+1:len(base2)]
            # 뒤집어 넣기
            # tmp = tmp[i+1:len(base2)]+'0'+tmp[:i]
        else:
            tmp = tmp[:i] + '1' + tmp[i + 1:len(base2)]
        base2_arr.append(tmp)
    for i in range(len(base3)):
        tmp = base3
        tmp2 = base3
        if tmp[i] == '1':
            tmp = tmp[:i] + '0' + tmp[i + 1:len(base3)]
            tmp2 = tmp[:i] + '2' + tmp[i + 1:len(base3)]
        elif tmp[i] == '0':
            tmp = tmp[:i] + '1' + tmp[i + 1:len(base3)]
            tmp2 = tmp[:i] + '2' + tmp[i + 1:len(base3)]
        else:
            tmp = tmp[:i] + '0' + tmp[i + 1:len(base3)]
            tmp2 = tmp[:i] + '1' + tmp[i + 1:len(base3)]
        base3_arr.append(tmp)
        base3_arr.append(tmp2)
    # print(base2_arr, base3_arr)
    # 진수를 10진수로 변환하는 과정
    for i in range(len(base2_arr)):
        tmp_val = 0
        for j in range(len(base2)):
            tmp_val += int(base2_arr[i][j])*(2**(len(base2)-j-1))
        base2_values.append(tmp_val)
    for i in range(len(base3_arr)):
        tmp_val = 0
        for j in range(len(base3)):
            tmp_val += int(base3_arr[i][j])*(3**(len(base3)-j-1))
        base3_values.append(tmp_val)
    # print(base2_values, base3_values)
    ans = 0
    for i in range(len(base2_values)):
        flag = False
        for j in range(len(base3_values)):
            if base2_values[i] == base3_values[j]:
                ans = base2_values[i]
                flag = True
                break
        if flag:
            break
    print('#{} {}'.format(t+1, ans))

# for tc in range(1, int(input()) + 1):
#     binary = input()
#     ternary = input()
#
#     n = len(binary)
#     m = len(ternary)
#
#     tmp_b = []
#     btod = int(binary, 2)
#     for i in range(n):
#         tmp_b.append(btod ^ (1 << i))
#     # print(tmp_b)
#
#     idx = 0
#     res = False
#     while idx < m:
#         t_list = list(ternary)
#
#         for i in range(3):
#             t_list[idx] = str(i)
#             tmp_t = int(''.join(t_list), 3)
#             # print(tmp_t)
#
#             if tmp_t in tmp_b:
#                 res = tmp_t
#         if res:
#             break
#
#         idx += 1
#
#     print(f'#{tc} {res}')

# T = int(input())
# for test_case in range(1, T + 1):
#     n_2 = list(input())
#     n_3 = list(input())
#     chk = []
#     for i in range(len(n_2)):
#         if n_2[i] == '1':
#             n_2[i] = '0'
#             chk.append(int(''.join(n_2), 2))
#             n_2[i] = '1'
#         else:
#             n_2[i] = '1'
#             chk.append(int(''.join(n_2), 2))
#             n_2[i] = '0'
#     res = 0
#     for i in range(len(n_3)):
#         d = ['0', '1', '2']
#         origin = n_3[i]
#         d.remove(n_3[i])
#         for j in d:
#             n_3[i] = j
#             tmp = int(''.join(n_3), 3)
#             if tmp in chk:
#                 res = tmp
#                 break
#         if res != 0:
#             break
#         n_3[i] = origin
#
#     print('#{} {}'.format(test_case, res))