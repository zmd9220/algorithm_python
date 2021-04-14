for t in range(1, 11):
    arr = [0] * 101
    dump = int(input())
    ls = list(map(int, input().split()))
    # 카운팅 배열 작업
    for i in ls:
        arr[i] += 1
    min_i = 0
    max_i = 0
    while dump > 0:
        # 덤프 작업은 기본적으로 높이가 가장 낮은 것에 +1(다음 카운팅 인덱스로 이동), 가장 높은 것에 -1(바로 앞 카운팅 인덱스로 이동)
        # 0에서 부터 시작(높이가 작은 쪽)하는 쪽의 가장 작은 건물의 idx를 찾기(높이)
        for j in range(1, len(arr)):
            if arr[j] > 0:
                min_i = j
                break
        # 가장 큰 건물의 높이를 찾기(idx, 오름차순이므로 역순으로 탐색하면 됨)
        for j in range(len(arr)-1, 0, -1):
            if arr[j] > 0:
                max_i = j
                break
        # 가장 큰 건물과 작은 건물의 차이가 없거나(이미 평탄화 끝), 1인 경우(평탄화를 해도 왔다갔다 할 뿐 의미가 없음) 종료
        if (max_i - min_i) == 0 or (max_i - min_i) == 1:
            print(f'#{t} {max_i - min_i}')
            break
        # 그 외에는 덤프 작업 진행(덤프 횟수도 줄이고)
        arr[min_i] -= 1
        arr[min_i+1] += 1
        arr[max_i] -= 1
        arr[max_i-1] += 1
        dump -= 1
    # 마지막 덤프 작업이 끝나고 만약 현재 가르키는 인덱스 위치의 건물이 0(해당 높이의 건물이 없음)이 되었을 때, 다음 인덱스로 이동
    if arr[min_i] == 0:
        min_i += 1
    if arr[max_i] == 0:
        max_i -= 1
    print(f'#{t} {max_i-min_i}')