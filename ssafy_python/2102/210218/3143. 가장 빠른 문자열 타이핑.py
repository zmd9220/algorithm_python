# 처음 생각한 방법은 브루트 포스로 검사하기 였는데 풀어보니 abababa aba와 같은 경우 정답을 7으로 출력함
# 즉 aba가 나오면 그 다음인 4번째 인덱스인 a[3]부터 검사해야 되는데 브루트 포스로 짜다보니 a[1]를 검색해서 이후
# a[2] 부터 aba가 나오므로 값이 추가되는 문제가 발생함 그래서 for문이 아닌 while로 하고 idx를 개별 관리 시행
# 맞는 문자열이 나오면 다음부터 살피도록 변경함
for t in range(int(input())):
    a, b = input().split()
    cnt = 0
    idx = 0
    # 전체 인덱스 탐색범위는 a-b의 길이 - 그외에는 b보다 작은 문자열만 생성됨
    while idx <= len(a)-len(b):
        found = True
        for j in range(len(b)):
            if a[idx+j] != b[j]:
                found = False
                idx += 1
                break
        if found:
            cnt += 1
            # 찾았으면 찾은곳+b크기(왜냐면 b문자열이 존재하니까 탐색X) 이후부터 탐색하도록 변경
            idx += len(b)
    print('#{} {}'.format(t+1, len(a)-(len(b)-1)*cnt))