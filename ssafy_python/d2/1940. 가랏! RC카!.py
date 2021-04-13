
for t in range(int(input())):
    N = int(input())
    now_spd = 0
    distance = 0
    for n in range(N):
        # 어쩔땐 1개만 받고 어쩔땐 2개만 받으므로 따로 변수를 지정하기 어려움..
        cmd = list(map(int, input().split()))
        # cmd == 0 일땐 현재 속도만큼 거리를 더하면 됨 나머지는 속력 변화도 반영
        if cmd[0] == 1:
            now_spd += cmd[1]
        elif cmd[0] == 2:
            # 줄일 속도가 현재 속도보다 크면 0이 되는 것을 처리해야함(음수인 속도는 존재x)
            if now_spd - cmd[1] > 0:
                now_spd -= cmd[1]
            else:
                now_spd = 0
        distance += now_spd
    print(f'#{t+1} {distance}')

