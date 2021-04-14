# 파이썬의 경우 큐를 만들기 쉽지만 다른 언어를 생각해 idx를 이용해 구현해보기
# 단순히 문제'만'풀기 위함이면 도는갯수/배열크기 한 나머지를 + 하면 그게 정답일것(크기만큼 원래자리로 계속돌아오니)
# 그런데 이번엔 큐 연습을 할겸 일일히 바꿔보겠음
for t in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    # 일반적인 큐 처럼 매번 땡긴다면
    # for i in range(m):
    #     tmp = arr[0]
    #     # 한칸씩 앞으로
    #     for j in range(1, n):
    #         arr[j-1] = arr[j]
    #     arr[n-1] = tmp
    # print('#{} {}'.format(t+1, arr[0]))

    # 단순하게 답을 구할 생각이라면
    # print('#{} {}'.format(t+1, arr[m % n]))

    # 파이썬 버전으로 한다면
    for i in range(m):
        arr.append(arr.pop(0))
    print('#{} {}'.format(t + 1, arr[0]))