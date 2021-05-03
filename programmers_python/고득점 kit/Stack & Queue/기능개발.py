
# https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []
    idx = 0
    while progresses:
        progresses[idx] += speeds[idx]
        idx += 1
        if idx == len(progresses):
            idx = 0
            # 맨 앞이 100이상이 되면 꺼내는 조건이 됨
            if progresses[0] >= 100:
                cnt = 0
                while progresses and progresses[0] >= 100:
                    progresses.pop(0)
                    speeds.pop(0)
                    cnt += 1
                answer.append(cnt)
    return answer

pro = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(pro, speeds))