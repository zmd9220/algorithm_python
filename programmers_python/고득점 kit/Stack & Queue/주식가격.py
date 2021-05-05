def solution(prices):
    answer = [0] * len(prices)
    idx = 0
    while idx < len(prices) - 1:
        upper_time = 1
        now_value = prices[idx]
        for i in range(idx + 1, len(prices) - 1):
            if prices[i] >= now_value:
                upper_time += 1
            else:
                break
        answer[idx] = upper_time
        idx += 1

    return answer