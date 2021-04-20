
def quick_sort(data, pivot_idx, last_idx):
    i = pivot_idx + 1
    j = last_idx
    # pivot이 마지막보다 작을 때만 last보다 크거나 같아지는 순간 정렬은 끝
    if pivot_idx < last_idx:
        # j <= i 될때까지 반복
        while True:
            # i가 마지막 인덱스를 넘지 못하게(인덱스 에러 or 무한 루프 방지) + i는 피벗기준 큰 값을 유지할 것 -> j와 교환할 때 피벗 뒤에 위치해야 하므로
            while i < last_idx and data[i] < data[pivot_idx]:
                i += 1
            # j가 피벗까지 못하게 (무한 루프에 빠질 수 있음) + j는 피벗기준 작은 값을 유지할 것 -> i 또는 피벗과 교환할 것이므로
            while j > pivot_idx and data[j] > data[pivot_idx]:
                j -= 1
            if j <= i:
                # j 가 새로운 피벗이 되는 시점
                data[j], data[pivot_idx] = data[pivot_idx], data[j]
                # j와 현재 피벗값의 위치가 바뀌는 순간 현재 피벗값은 그 자리가 정렬된 자리이므로 더 이상 건들 이유가 없음
                quick_sort(data, pivot_idx, j-1)
                quick_sort(data, j+1, last_idx)
                break
            else:
                # 아직 현재 피벗 내에서 정렬이 가능한 경우 -> i, j 를 체인지
                data[j], data[i] = data[i], data[j]
                j -= 1
                i += 1
        return


for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, len(arr)-1)
    # print(arr)
    print('#{} {}'.format(t+1, arr[n//2]))

