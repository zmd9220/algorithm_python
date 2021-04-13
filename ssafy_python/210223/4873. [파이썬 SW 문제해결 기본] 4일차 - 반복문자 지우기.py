# 문제에선 길이만 구하면 되므로 스택으로 뒤집어서 풀던 그대로 풀던 상관이없음
# 다만 가능하면 원본문자열도 살리는 방향으로 구성해보겠음
# 앞에서부터 넣던 뒤에서부터 넣던 요는 넣을때 일단 최상단(가장 최근에 들어간 문자)에 나와 같은 문자가 있는지를 체크
def chk_repeat(words):
    st = [] # 스택처럼 쓸 리스트
    for i in range(len(words)):
        # 비었을땐 일단 삽입
        if not len(st):
            st.append(words[i])
        # 비어있지 않을 경우(스택안에 값이 존재)
        else:
            # 지금 문자와 최근 스택에 들어간 문자가 같다면 중복문자
            if words[i] == st[-1]:
                st.pop()
            # 같지 않으면 스택에 추가(현재는 중복 문자가 아니므로)
            else:
                st.append(words[i])
    # 작업 종료후 스택의 길이 = 문자열의 길이 반환
    return len(st)


for t in range(int(input())):
    test_words = input()
    result = chk_repeat(test_words)
    print('#{} {}'.format(t+1, result))

