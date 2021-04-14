
T = int(input())

for t in range(T):
    n, m = map(int, input().split())
    ls = list(map(int, input().split()))

    # 최대값, 최소값
    max_sum = -1
    min_sum = 10000000

    # 구간합을 위한 인덱스 탐색용 변수
    idx = 0
    while True:
        if idx+m > n:
            break
        now_sum = 0
        for i in range(idx, idx+m):
            now_sum += ls[i]
        if now_sum > max_sum:
            max_sum = now_sum
        if now_sum < min_sum:
            min_sum = now_sum
        idx += 1

    print(f'#{t + 1} {max_sum-min_sum}')





    # 구간합이 붙어있는 이웃끼리만 이구나.. 정렬이 아닌 받은 리스트 대로 확인하면서 풀어야함; 그리디
    # for i in range(0, len(ls)-1):
    #     for j in range(i+1, len(ls)):
    #         if ls[i] > ls[j]:
    #             ls[i], ls[j] = ls[j], ls[i]
    #
    # for i in range(m):
    #     min_sum += ls[i]
    # for i in range(len(ls)-1, len(ls)-m-1, -1):
    #     max_sum += ls[i]
    # result = max_sum - min_sum



    # 문제에 중복된 값이 있다고 생각했는데 없나봄
    # arr = [0] * 10001 # 카운팅 배열
    # for i in ls:
    #     arr[i] += 1
    # cnt = m
    # minArr = arr[:]
    # while cnt > 0:
    #     for i in range(len(minArr)):
    #         if minArr[i] > 0:
    #             min_sum += i
    #             minArr[i] -= 1
    #             cnt -= 1
    #             break
    # cnt = m
    # maxArr = arr[:]
    # while cnt > 0:
    #     for i in range(len(maxArr)-1, -1, -1):
    #         if maxArr[i] > 0:
    #             max_sum += i
    #             maxArr[i] -= 1
    #             cnt -= 1
    #             break
    # result = max_sum - min_sum

