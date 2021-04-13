def tournament(data, start, end):
    if start == end:
        return start
    first = tournament(data, start, (start+end)//2)
    second = tournament(data, (start+end)//2+1, end)
    # 보, 가위인 경우(1,3)인 경우만 작은 수가 이기고 나머지 경우는 큰 수가 이김
    if (data[first-1] == 3 and data[second-1] == 1) or (data[first-1] == 1 and data[second-1] == 3):
        return first if data[first-1] < data[second-1] else second
    else:
        return first if data[first-1] >= data[second-1] else second

for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print('#{} {}'.format(t+1, tournament(arr, 1, n)))