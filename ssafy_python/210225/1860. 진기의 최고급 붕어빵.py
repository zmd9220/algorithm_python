# 현재 시간 기준으로 만든 전체 빵 갯수 > 나눠줄 사람 수보다 큰 경우가 계속 유지되어야만 대기 없이 판매 가능
def is_possible(n, m, k, arr):
    # 나의 경우, 가장 늦게 오는 사람의 시간 부터 뒤로 검색할 예정(빵 제공 가능한지 여부체크)
    for i in range(len(arr)-1, -1, -1):
        # 만약 마지막에 오는사람까지 전체를 포함하여 현재 기준 빵 재고량이 충분한지 여부
        if n > (arr[i]//m)*k:
            return 'Impossible'
        n -= 1
    return 'Possible'


for t in range(int(input())):
    n, m, k = map(int, input().split())
    peoples = list(map(int, input().split()))
    # 일단 사람들을 오는 시간 순으로 정렬
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if peoples[min_idx] > peoples[j]:
                min_idx = j
        peoples[i], peoples[min_idx] = peoples[min_idx], peoples[i]
    print('#{} {}'.format(t+1, is_possible(n, m, k, peoples)))
