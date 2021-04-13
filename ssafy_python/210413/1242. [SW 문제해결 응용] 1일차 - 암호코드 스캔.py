
# import sys
# sys.stdin = open("sample_input.txt", "r")

hex_table = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111',
}

reduce_table = {
    '211': 0, '221': 1, '122': 2,
    '411': 3, '132': 4, '231': 5,
    '114': 6, '312': 7, '213': 8,
    '112': 9,
}


def check_code(data, find_arr):
    odd = 0
    even = 0
    result = 0
    for i in range(len(data)-1):
        result += data[i]
        # 질문상으론 짝수 -> 배열상으론 홀수
        if i % 2:
            even += data[i]
        else:
            odd += data[i]
    result += data[-1]
    even += data[-1] + (odd * 3)
    # 나머지가 존재 = 10의 배수가 아님 비정상
    if even % 10 == 0 and data not in find_arr:
        return result
    else:
        return 0


def reduce_and_decode(fst, snd, trd):
    min_val = min(fst, snd, trd)
    fst //= min_val
    snd //= min_val
    trd //= min_val
    string = str(fst)+str(snd)+str(trd)
    return reduce_table[string]


for t in range(int(input())):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    binary_arr = [''] * n
    find = []
    ans = 0
    for i in range(n):
        for j in range(m):
            binary_arr[i] += hex_table[arr[i][j]]
    # print(binary_arr)
    decode = []
    for i in range(n):
        # 전체 암호코드 숫자들은 0, 1, 0, 1 이 몇번 나오냐에 차이일 뿐 0, 1, 0, 1의 값으로 나오는 것은 동일하다.
        first, second, third = 0, 0, 0
        for j in range(m*4-1, -1, -1):
            # 뒤에서 가장 처음 만나는 1 = 해당 암호코드 숫자를 디코딩하기 위한 코드 중 맨 뒤의 1(이게 56의 몇배수냐에 따라 1이 몇번나올지 모름)
            if first == 0 and second == 0 and binary_arr[i][j] == '1':
                third += 1
            elif third >= 1 and first == 0 and binary_arr[i][j] == '0':
                second += 1
            elif third >= 1 and second >= 1 and binary_arr[i][j] == '1':
                first += 1
            # 위의 3 조건에 걸리지 않는 경우는 0 1 0 1 에서 0번째 차례가 나올 때 or 지금 third가 0일 때
            if first > 0 and second > 0 and third > 0 and binary_arr[i][j] == '0':
                decode.append(reduce_and_decode(first, second, third))
                first, second, third = 0, 0, 0

            if len(decode) == 8:
                # 뒤에서부터 탐색했으므로 배열도 거꾸로 되어있으므로 원래 상태로 돌리기
                decode = decode[::-1]
                # 암호코드인지 + 이미 나왔던 암호코드인지 확인
                decode_value = check_code(decode, find)
                # 중복 방지용 배열
                find.append(decode)
                ans += decode_value
                decode = []

    print('#{} {}'.format(t+1, ans))






# 1. 암호코드를 가진 데이터를 뽑기 - 관찰을 통해 알아낸 사실 -> 암호코드의 범위는 0이 아닌수 ~ 0이되는수 직전까지
# 2. 암호코드는 길이에 따라 56배수로 존재 -> 암호코드의 전체 길이에 따라 56의 몇 곱인지 확인하고, 해당 곱에 따라 다시 56길이의 문자열로 재구성 해야함
# 이후의 진행방식은 어제 풀었던 방법과 같음



# a = '328D1AF6E4C9BB'
# b = '1DB176C588D26EC'
# c = '196EBC5A316C578'
# print(len('1DB176C588D26EC'))
# print(len('328D1AF6E4C9BB'))
# print(len('196EBC5A316C578'))
#
# tmp = ''
# for i in range(len(c)):
#     tmp += hex_table[c[i]] + ' '
# print(tmp)

# 0001 1001 0110 1110 1011 1100 0101 1010 0011 0001 0110 1100 0101 0111 1000

# 01110110 11000101 110110110 00101100 010001101 00100110 111011
# (00)01 1101 1011 0001 0111 0110 1100 0101 1000 1000 1101 0010 0110 1110 11(00) 1

# print(len('3C33C0CC0F0C3C0F3033CFCF3CFC'))
# print(len('1FE1E1FFE1FE1FE1FFE01FE01E1FE001E1FE1FFE1E1FFFE1FFE1FE'))
# def make_binary(datas):
#     result = []
#     for i in range(len(datas)):
#         tmp_code = datas[i]
#         tmp_decode = ''
#         for j in range(len(tmp_code)):
#             tmp_decode += hex_table[tmp_code[j]]
#         print(len(tmp_decode))
#         print(tmp_decode)
#         for j in range(len(tmp_decode)-1, -1, -1):
#             if tmp_decode[j] != '0':
#                 multiple = len(tmp_decode) // 56
#                 start_idx = j - (56 * multiple - 1)
#                 # print(j, (56 * (len(tmp_decode) // 56) - 1))
#                 # print(start_idx)
#                 if start_idx < 0:
#                     start_idx = 0
#                 tmp_decode = tmp_decode[start_idx:j+1]
#                 break
#         result.append(tmp_decode)
#     return result
#
# for t in range(int(input())):
#     n, m = map(int, input().split())
#     arr = [input() for _ in range(n)]
#     codes = []
#     for i in range(n - 1, -1, -1):
#         tmp = ''
#         for j in range(m - 1, -1, -1):
#             if arr[i][j] != '0':
#                 tmp = arr[i][j] + tmp
#             # 0이 나올 때의 2가지 케이스 1. tmp 가 차있거나 2. 비어있거나
#             else:
#                 if tmp:
#                     if j-1 >= 0 and arr[i][j-1] != '0':
#                         tmp = arr[i][j] + tmp
#                     # 넣기전에 이미 같은 코드가 있으면 넣을 필요가 없음
#                     elif not tmp in codes:
#                         codes.append(tmp)
#                         tmp = ''
#     codes.append('FF000F0F0FFFF0FFFF0F000F0FF0FF000F00FF00F0FF000F000FF0F')
#     print(codes)
#     decodes = make_binary(codes)
#     print(decodes)
