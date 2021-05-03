
# https://programmers.co.kr/learn/courses/30/lessons/42587
def solution(priorities, location):
    # 카운트 할 정답
    answer = 0
    while len(priorities):
        tmp = priorities.pop(0)
        flag = True
        for i in range(len(priorities)):
            if priorities[i] > tmp:
                flag = False
                priorities.append(tmp)
                if location == 0:
                    location = len(priorities) - 1
                else:
                    location -= 1
                break
        if flag:
            answer += 1
            if location == 0:
                break
            else:
                location -= 1
    return answer