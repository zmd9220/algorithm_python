# 일반적인 괄호검사에서 {}랑 ()를 구분하여 처리하기, 스택넣어서 확인하고 꺼냈을때 ()나 {}가 매칭되는지 확인
def matching(words):
    st = [] # 괄호 검사용 리스트(스택처럼 사용할 예정)
    # 뒤에서 부터 괄호 검사
    for i in range(len(words)-1, -1, -1):
        # )나 }는 스택에 넣기
        if words[i] == ')' or words[i] == '}':
            st.append(words[i])
        # (인 경우
        elif words[i] == '(':
            # 먼저 스택안에 아무것도 없는경우 ) } 둘다 안들어왔으므로 검사 탈락
            if not len(st):
                return 0
            char = st.pop()
            # )가 아니면 괄호검사 탈락
            if char != ')':
                return 0
        # {도 위와 같이 진행
        elif words[i] == '{':
            # 먼저 스택안에 아무것도 없는경우 ) } 둘다 안들어왔으므로 검사 탈락
            if not len(st):
                return 0
            char = st.pop()
            if char != '}':
                return 0
    # 모든 조건이 돌고 스택에 괄호가 남아있는지 확인 남으면 검사 탈락
    if len(st):
        return 0
    else:
        return 1


for t in range(int(input())):
    result = matching(input())
    print('#{} {}'.format(t+1, result))