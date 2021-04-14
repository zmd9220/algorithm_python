
# nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

# find나 index 사용하면 쉽겠지만 없이해보기
# 일반 버블 정렬이나 셀렉션 정렬을 find, idx 함수 없이 사용할 경우
nums = [["ZRO", 0], ["ONE", 1], ["TWO", 2], ["THR", 3], ["FOR", 4],
        ["FIV", 5], ["SIX", 6], ["SVN", 7], ["EGT", 8], ["NIN", 9]]

for t in range(int(input())):
    # 생각해보니 카운팅으로 풀어도 될듯 카운트를 초기화 해야하므로 여기 안에 넣어야함
    counting = [0] * 10
    n, k = input().split()
    k = int(k)
    arr = list(input().split())

    for i in range(k):
        for ch in range(len(nums)):
            if arr[i] == nums[ch][0]:
                counting[nums[ch][1]] += 1
        result = []
    for i in range(len(counting)):
        for j in range(counting[i]):
            result.append(nums[i][0])
    print(n)
    print(f' {" ".join(result)}')

    # 풀리긴 하는데 시간초과됨
    for i in range(len(arr)-1):
        min_idx = i
        min_value = 0
        for ch in range(len(nums)):
            if arr[i] == nums[ch][0]:
                min_value = nums[ch][1]
                break
        for j in range(i+1, len(arr)):
            j_value = 0
            for ch in range(len(nums)):
                if arr[j] == nums[ch][0]:
                    j_value = nums[ch][1]
                    break
            if j_value < min_value:
                min_idx = j
                min_value = j_value
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    print(n)
    print(f'{" ".join(arr)}')