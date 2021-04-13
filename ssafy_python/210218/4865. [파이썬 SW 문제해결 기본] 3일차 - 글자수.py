# 이 문제가 단어까지 범위를 둘진 모르겠으나 단순히 1글자만 본다면 최대값을 구해도되고 단어라고 해도 1글자일 경우가 가장 수가 많을것.
# 그러므로 각 글자마다 전체 탐색을 하며 문자 찾기
for t in range(int(input())):
    n = input()
    m = input()
    cnt = 0
    # 브루트 포스
    for i in range(len(n)):
        tmp_cnt = 0
        for j in range(len(m)):
            if n[i] == m[j]:
                tmp_cnt += 1
        if cnt < tmp_cnt:
            cnt = tmp_cnt
    print('#{} {}'.format(t+1, cnt))