for t in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort(key=lambda x: (x[1], x[0]))
    # 이번 문제의 그리디는 가장 종료시간이 짧은 친구를 첫 화물차로 뽑고 해당 시간과 겹치는 모든 수를 제거,
    # 그리고 다음으로 오는 가장 종료시간이 빠른 친구를 다음 화물차로 지정
    # 이것을 반복
    idx = 0
    search = 1
    # ans = 1
    while True:
        # 찾음 해당하는 화물차의 시작시간이 이전 화물차의 작업시간과 겹치지 않을 때 -> 가장 들어올 수 있는 최선의 다음 화물차
        if arr[idx][1] <= arr[search][0]:
            # ans += 1
            idx = search
            search += 1
        # 겹칠 때 = 제거
        else:
            arr.pop(search)
        if search == len(arr):
            break
    print('#{} {}'.format(t+1, search))


