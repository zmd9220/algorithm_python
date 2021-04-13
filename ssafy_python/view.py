
# min 등 기본 함수 가능한 배제하고 풀기
for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    # 전체 범위는 앞2개, 뒤2개는 비게 되므로 2번째 인덱스에서 마지막 2번째전까지
    for i in range(2, len(arr)-2):
        window = 0
        # 1단계 조건(바로 옆건물이 나보다 큰지 작은지 여부(그래야 2단계 확보가능)
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            left = arr[i] - arr[i-1]
            right = arr[i] - arr[i+1]
            if left > right:
                window = right
            else:
                window = left
            # 2단계 조건(바로 옆옆 건물이 나보다 큰지 작은지)
            if arr[i] > arr[i-2] and arr[i] > arr[i+2]:
                left = arr[i] - arr[i-2]
                right = arr[i] - arr[i+2]
                if window > left:
                    window = left
                # 왼쪽이 바로옆 건물보다 작을경우 위에서 이미 윈도우를 left 값으로 변경
                # 즉 그럼에도 밑의 if 문이 작동한다는건 바로옆 건물의 최소값 > 2칸거리의 건물 왼쪽 > 오른쪽
                if window > right:
                    window = right
            # 한쪽이라도 나보다 큰 경우 조망권은 절대 확보 될 수 없다.
            else:
                window = 0
        # 계산이 끝나면 세대 수 추가
        cnt += window
    # 작업이 끝나면 현재 케이스와 전체 카운트 출력
    print(f'#{tc} {cnt}')

# for tc in range(1, 11):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     cnt = 0
#
#     for i in range(2, N-2):
#         MAX = max(arr[i-2], arr[i-1], arr[i+1], arr[i+2])
#
#         if arr[i] - MAX >0:
#             cnt += (arr[i]-MAX)
#     print('#{} {}'.format(tc, cnt))


