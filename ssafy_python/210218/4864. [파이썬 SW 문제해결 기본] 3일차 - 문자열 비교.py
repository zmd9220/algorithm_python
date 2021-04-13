# 문자열 비교 방법은 4가지 이상 존재하지만 우리가 크게 쓸건 브루트포스, kmp, 보이어-무어 3가지를 기반으로 진행(카프-라빈은 나중에 개인적으로)
for t in range(int(input())):
    n = input()
    m = input()
    result = 0
    # 1. 브루트 포스
    for i in range(len(m)):
        if m[i] == n[0]:
            flag = True
            for j in range(1, len(n)):
                if i+j >= len(m) or m[i + j] != n[j]:
                    flag = False
                    break
            if flag:
                result = 1
                break
    print('#{} {}'.format(t + 1, result))

    # 3. 보이어 무어 - 현재 인덱스 기준으로 문자가 확인 문자열(n)내에 있는지 확인후 있으면 해당 위치만큼 쉬프트,
    # 아닐경우 확인할 문자크기(n)만큼 바로 점프
    # now_idx = len(n)-1
    # while now_idx < len(m):
    #     # 확인 문자열 내에 해당 문자가 있는지 없는지 체크
    #     chk = False
    #     for i in range(len(n)-1, -1, -1):
    #         if m[now_idx] == n[i]
    #             now_idx += i


    # for i in range(0, len(m), len(n)):
    #     print(m[i])