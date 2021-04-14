# 기본 아이디어 현재 가격중 최대값을 구하고 그 최대값 인덱스 앞은 모두 구매 후 팔기
# 그리고 최대값 인덱스 이후부터 새로운 최대값 인덱스를 찾고 그 최대값 인덱스 앞을 모두 구매 후 팔기
# 이것을 마지막 인덱스 도착까지 반복
for t in range(int(input())):
    n = int(input())
    prices = list(map(int, input().split()))
    best_price_idx = 0
    used_idx = 0
    result = 0
    while best_price_idx < len(prices):
        # 최대값을 가진 인덱스 찾는 과정
        for i in range(best_price_idx, len(prices)):
            if prices[i] > prices[best_price_idx]:
                best_price_idx = i
        # 해당인덱스 이전 모든 인덱스는 다 더해주면됨
        for i in range(used_idx, best_price_idx):
            result += prices[best_price_idx] - prices[i]
        # 이후 최대값 인덱스까지 사용됐음을 적용하고 최대값 인덱스+1을 하여 다시 그 지점부터 끝까지 탐색
        best_price_idx += 1
        used_idx = best_price_idx
    print('#{} {}'.format(t+1, result))

# 스택이면 좀더 쉬울려니?

# T = int(input())
# for test_case in range(1,T+1):
#     N = input()
#     arr = list(map(int,input().split()))
#     res = 0
#     max = 0
#     while arr :
#         t = arr.pop(-1)
#         if max <= t :
#             max = t
#         else:
#             res += max-t
#     print('#{} {}'.format(test_case,res))
