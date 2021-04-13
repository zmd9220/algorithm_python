import sys



def solution(new_id):
    answer = new_id.lower()
    # print(answer)

    spec = '~!@#$%^&*()=+[{]}:?,<>'
    for char in spec:
        answer = answer.replace(char, "")

    tmp_ans = ""
    tmp_ans +=answer[0]
    for i in range(1, len(answer)):
        test = answer[i-1]
        if test == ".":
            if answer[i] != ".":
                tmp_ans += answer[i]
        else:
            tmp_ans += answer[i]
    answer = tmp_ans

    answer = answer.strip('.')
    # print(answer)

    if not answer:
        answer += 'a'
        # print(answer)

    if len(answer) >= 16:
        answer = answer[0:15]
        # print(answer)
        answer = answer.strip('.')

    if len(answer) <= 2:
        while (len(answer) != 3):
            answer += answer[-1]
            # print(answer)


    return answer

new_id1 = "...!@BaT#*..y.abcdefghijklm"
print(solution(new_id1))