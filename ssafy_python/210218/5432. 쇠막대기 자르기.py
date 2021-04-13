# 리스트로 푸는법
for t in range(int(input())):
    irons = input()
    laser = 0
    now_iron = 0
    result = 0
    idx = 0
    while idx < len(irons):
        if irons[idx] == '(':
            if irons[idx+1] == ')':
                result += now_iron
                idx += 1
            else:
                now_iron += 1
        else:
            result += 1
            now_iron -= 1
        idx += 1

    print('#{} {}'.format(t+1, result))
# 스택으로 푸는법
