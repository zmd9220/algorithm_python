for t in range(1, 11):
    n = int(input())
    test = input()
    stack = [] # 피연산자 관리
    postfix = '' # 후위 계산식
    for char in test:
        # 숫자는 그냥 넣음
        if char.isdigit():
            postfix += char
        # 현 문제에서 피연산자는 +, * 두가지 경우
        # +의 경우 자신보다 낮은 연산자는 없으므로 다 내보냄(스택이 빌때까지)
        elif char == '+':
            while len(stack):
                postfix += stack.pop()
            # 다 내보내면 이번에 만난 + 연산자 넣기
            stack.append(char)
        # *의 경우 +를 만나기전까지만 pop이 진행됨
        # 즉 *는 스택이 비어있지않고(비어있으면 뺄게 없음 바로 삽입) 내 앞의 피연산자가 +가 아닌 모든것을 빼기(여기선 *만)
        else:
            while len(stack) and stack[-1] != '+':
                postfix += stack.pop()
            # +를 만났거나 남은 피연산자가 없다(스택이 비었다)면 * 연산자 넣기
            stack.append(char)
    # 남은 스택 피연산자는 뒤에 다 몰아넣기
    while len(stack):
        postfix += stack.pop()
    # stack은 어차피 비었을테니 계산할 때 재활용
    for char in postfix:
        if char.isdigit():
            stack.append(int(char))
        # 연산 순서에 주의 b가 먼저 꺼내지는 놈 즉 계산상에서 뒤에 위치하는 수가 됨 그래서 b라고 지칭한것
        elif char == '+':
            b = stack.pop()
            a = stack.pop()
            stack.append(a+b)
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(a*b)
    print('#{} {}'.format(t, stack.pop()))