
for t in range(1, 11):
    tc = int(input())
    word = input()
    string = input()
    ans = 0
    # 일단 가장 기초적인 방법 첫문자가 같으면 뒤에 탐색
    for i in range(len(string)):
        flag = False
        if string[i] == word[0]:
            flag = True
            for j in range(1, len(word)):
                # 뒤로 가서 하나씩 탐색
                if (i+j >= len(string)) or string[i+j] != word[j]:
                    flag = False
                    break
        # 찾은 경우
        if flag:
            ans += 1

    print('#{} {}'.format(tc, ans))
