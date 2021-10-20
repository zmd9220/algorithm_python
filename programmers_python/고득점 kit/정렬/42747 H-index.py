def solution(citations):
    answer = 0
    arr = sorted(citations)
    print(arr)
    h_count = 0
    for i in range(arr[-1], -1, -1):
        for j in range(len(arr) - 1, -1, -1):
            if i <= arr[j]:
                h_count += 1
        if h_count >= i:
            answer = i
            break
        h_count = 0

    #     for i in range(len(arr)):
    #         is_h = False
    #         # 인용된 논문 수
    #         h_count = len(arr)-i

    #         # 나머지 논문
    #         remain_count = i

    #         print(h_count, remain_count)
    #         if h_count < arr[i]:
    #             break
    #         # for j in range(i+1, len(arr)):
    #         if remain_count <= arr[i]:
    #             answer = arr[i]

    return answer