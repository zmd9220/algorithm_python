
for t in range(1, 11):
    n = int(input())
    test_case = input()
    stack = []
    postfix = []
    # 후위 표기식으로 변경 작업
    for i in range(n):
        # 괄호일 경우 괄호 전까지 모든 연산자 꺼내기
        if test_case[i] == ')':
            # 만약 괄호의 유효성 따지면 이것도 추가 if not flag:
            while len(stack):
                if stack[-1] == '(':
                    stack.pop()
                    break
                else:
                    postfix.append(stack.pop())
        # 여는 괄호는 일단 넣기(나중에 괄호 범위를 잡기위해)
        elif test_case[i] == '(':
            stack.append(test_case[i])
        # 숫자인 경우 0~9
        elif ord('0') <= ord(test_case[i]) <= ord('9'):
            postfix.append(test_case[i])
        # + 일경우 앞이 괄호거나 스택이 빌때까진 계속 빼냄 순위가 (가 낮음
        elif test_case[i] == '+':
            while len(stack) and stack[-1] != '(':
                postfix += stack.pop()
            # 다 내보내면 이번에 만난 + 연산자 넣기
            stack.append(test_case[i])
        # * 일경우 앞이 괄호거나 스택이 비거나 + 일때까지 계속 빼냄 (와 +가 우선순위가 낮음
        elif test_case[i] == '*':
            while len(stack) and stack[-1] != '(' and stack[-1] != '+':
                postfix.append((stack.pop()))
            stack.append(test_case[i])
    while len(stack):
        postfix.append(stack.pop())
    # print(postfix)

    # 스택 비었으니 재활용해서 식 계산
    for char in postfix:
        # char = 숫자인 경우
        if ord('0') <= ord(char) <= ord('9'):
            stack.append(int(char))
        # char = 연산자인 경우
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            if char == '+':
                stack.append(op1 + op2)
            else:
                stack.append(op1 * op2)
    print('#{} {}'.format(t, stack.pop()))
