
for t in range(int(input())):
    arr = []
    # 그냥 일괄적으로 번호가 작은방에서 큰방으로 이동한다고 가정할것
    # 여기서 미리 처리안하면 나중에 if문 등을통해 현재방과 돌아갈 방 중 큰 방을 일일히 찾아야됨
    # 복도의 거리도 미리 구해놓기
    # 위아래의 크기도 같게 혹시 399 < 400이 되어버려서 같은 거리임에도 안될수 있으므로
    # 홀수일때는 +1을 하여 짝수와 같은 수로 맞춤 1=>2 399=>400
    for n in range(int(input())):
        start, end = map(int, input().split())
        if start % 2:
            start += 1
        if end % 2:
            end += 1
        if start > end:
            arr.append([end, start, start-end])
        else:
            arr.append([start, end, end-start])
    # 걍 오름차순 쓰자
    for i in range(len(arr)-1):
        mix_idx = i
        for j in range(i+1, len(arr)):
            # 시작지점도 크고 거리가 크거나 같을때
            if arr[mix_idx][2] > arr[j][2]:
                mix_idx = j
            elif arr[mix_idx][2] == arr[j][2]:
                if arr[mix_idx][0] < arr[j][0]:
                    continue
                mix_idx = j
        arr[mix_idx], arr[i] = arr[i], arr[mix_idx]
    # 이제부터 단위 시간 재기
    time = 0
    while len(arr):
        # 1 단위 시간 동안 일어날 일
        time += 1
        # 가장 처음이 가장 거리가 먼 친구(내림차순 정렬했으므로)의 시작점을 구하기(뒤는 볼 필요없음)
        max_start = arr.pop()[0]
        idx = 0
        for i in range(len(arr)-1, -1, -1):
            # 같은 1단위 시간내에 가장 큰 범위를 차지하는 친구와 서로 겹치지않는 다음으로 큰 친구가 있다면
            # (가장 큰친구의 시작점 > 다음으로 큰 친구의 도착점)
            # 꺼내고(방으로 보내고) 그 친구의 시작점(현재 나는 시작점이 무조건 작게끔 설정해둠)을 새로운 max로 설정
            if max_start > arr[i][1]:
                max_start = arr.pop(i)[0]

    print('#{} {}'.format(t+1, time))

# 해답을 찾아보니 그냥 최대로 겹치는 구간을 찾으면 그만큼은 무조건 빼야되니까 그게 총 단위시간이구나


