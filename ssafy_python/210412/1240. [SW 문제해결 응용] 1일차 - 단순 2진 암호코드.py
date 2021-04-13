
pwd_table = {
    '0001101': 0, '0011001': 1, '0010011': 2,
    '0111101': 3, '0100011': 4, '0110001': 5,
    '0101111': 6, '0111011': 7, '0110111': 8,
    '0001011': 9,
}

def check_code(data):
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
    if even % 10:
        return 0
    else:
        return result


for t in range(int(input())):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    pwd = ''
    pwd_code = []
    for i in range(n-1, -1, -1):
        find = False
        for j in range(m-1, -1, -1):
            if arr[i][j] == '1':
                pwd = arr[i][j-55:j+1]
                # print(len(pwd))
                # print(pwd)
                find = True
                break
        if find:
            break
    for i in range(0, len(pwd), 7):
        pwd_code.append(pwd_table[pwd[i:i + 7]])
    # print(pwd_code)
    ans = check_code(pwd_code)
    print('#{} {}'.format(t+1, ans))

