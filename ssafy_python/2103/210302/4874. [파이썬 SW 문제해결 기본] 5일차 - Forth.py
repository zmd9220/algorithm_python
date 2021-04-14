
def calculator(data):
    stack = []
    for i in range(len(data)):
        # 연산자의 경우 각각에 따라 진행
        # 사칙연산
        if data[i] == '+':
            # 먼저 연산자가 들어가기 전에 스택의 크기가 1이다 = 피연산자가 1개이므로 계산 불가 - 에러
            if len(stack) == 1:
                return 'error'
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(op1 + op2)
        elif data[i] == '-':
            if len(stack) == 1:
                return 'error'
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(op1 - op2)
        elif data[i] == '*':
            if len(stack) == 1:
                return 'error'
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(op1 * op2)
        elif data[i] == '/':
            if len(stack) == 1:
                return 'error'
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(op1 // op2)
        # .의 경우 종료인데 이때 스택의 크기가 1이 아니면 연산자 부족으로 에러
        elif data[i] == '.':
            if len(stack) == 1:
                return stack.pop()
            else:
                return 'error'
        # 숫자일경우 스택에 넣기
        else:
            stack.append(int(data[i]))


for t in range(int(input())):
    arr = list(input().split())
    print('#{} {}'.format(t+1, calculator(arr)))
