
ops = ['+', '-', '*', '/']


def brute():
    arr = [0] * 4
    perm([], arr)


def perm(opers, gen):

    if len(opers) == n-1:
        now_value = a[0]
        for i in range(len(opers)):
            if opers[i] == '+':
                now_value += a[i+1]
            elif opers[i] == '-':
                now_value -= a[i+1]
            elif opers[i] == '*':
                now_value *= a[i+1]
            elif opers[i] == '/':
                # 음수일 때와 양수일 때를 구분해야함
                if now_value < 0:
                    now_value = (abs(now_value) // a[i+1]) * -1
                else:
                    now_value = now_value // a[i+1]
        global max_value, min_value
        max_value = max(max_value, now_value)
        min_value = min(min_value, now_value)

    for i in range(4):
        
        if gen[i] < operators[i]:
            opers.append(ops[i])
            gen[i] += 1
            perm(opers, gen)
            opers.pop()
            gen[i] -= 1


n = int(input())
a = list(map(int, input().split()))
min_value = 10000000000
max_value = -10000000000
operators = list(map(int, input().split()))
brute()
print(max_value)
print(min_value)