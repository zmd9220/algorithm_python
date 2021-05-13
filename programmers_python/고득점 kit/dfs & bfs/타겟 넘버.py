def solution(numbers, target):
    answer = 0
    st = [(0, 0)]
    while st:
        value, cnt = st.pop()
        if cnt < len(numbers):
            st.append((value+numbers[cnt], cnt+1))
            st.append((value-numbers[cnt], cnt+1))
        else:
            if value == target:
                answer += 1
    return answer