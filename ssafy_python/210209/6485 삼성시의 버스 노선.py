T = int(input())
for t in range(T):
    bus = []
    station = []

    N = int(input())
    for n in range(N):
        a, b = map(int, input().split())
        bus.append([a, b])
        # print(bus)

    P = int(input())
    check = [0] * P
    for p in range(P):
        station.append(int(input()))
        # print(station)
    # 정렬이 필요없음
    # for i in range(len(station)-1, -1, -1):
    #     for j in range(i):
    #         if station[j] > station[j+1]:
    #             station[j], station[j+1] = station[j+1], station[j]

    # 해당 노선 내에 정류장이 존재하는지 확인후 체크에 플러스
    for i in range(len(station)):
        for bus_stop in bus:
            if bus_stop[0] <= station[i] <= bus_stop[1]:
                check[i] += 1

    print(f'#{t+1}', end=' ')
    for i in check:
        print(i, end=' ')
    print()



