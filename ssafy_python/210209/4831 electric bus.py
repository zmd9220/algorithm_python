
import sys
sys.stdin = open('../210216/input.txt', 'r')

T = int(input())
for t in range(T):
    k, n, m = map(int, input().split())
    bus_stop = list(map(int, input().split()))
    now_idx = n  # 현재 인덱스
    cnt = 0  # 몇번 정류장 들릴지 카운트
    while True:
        # 탈출 조건 1(현재 정류장 범위내인지)
        if now_idx == 0:
            print(f'#{t+1} {cnt}')
            break
        # k 범위 내에 없을 경우 0을 출력하기 위한 플래그
        flag = True
        # k칸 범위 내에 정류장이 있는지 탐색
        for i in range(k, 0, -1):
            # 0으로 도착(무사히 도착)
            if now_idx - i == 0:
                now_idx = 0
                flag = False
                break
            # 범위 내에 정류장이 있을 때
            if now_idx - i in bus_stop:
                now_idx = now_idx - i
                cnt += 1
                flag = False
                break
        # flag가 트루 범위 안에 있음
        if flag:
            print(f'#{t+1} 0')
            break



