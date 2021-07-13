def solution(S, C):
    # write your code in Python 3.6
    C1 = '@' + C.lower() + '.com>'
    S1 = S.split('; ')
    answer = []
    for i in range(len(S1)):
        words = S1[i].split(' ')
        if len(words[0]) > 8:
            word = words[0].replace('-', '')
            # print(word)
            username = word[:8].lower() + '.'
        else:
            username = words[0].lower() + '.'
        if len(words[-1]) > 8:
            word = words[-1].replace('-', '')
            # print(word)
            username += word[:8].lower()
        else:
            username += words[-1].lower()
        cnt = 2
        duplicate = username
        while duplicate in answer:
            duplicate = username + str(cnt)
            cnt += 1
        answer.append(duplicate)
    for i in range(len(S1)):
        S1[i] += ' <' + answer[i] + C1
    # print('; '.join(S1))
    return '; '.join(S1)


c = 'Example'
s = 'John Doe; Peter Benjamin Parker; Mary Jane Watson-Parker; John Elvis Doe; John Evan Doe; Jane Doe; Peter Brian Parker'
s1 = s.split('; ')
solution(s, c)
# print(s1)
# print(c.lower())


