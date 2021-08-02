
from collections import deque
from pprint import pprint

n, m = map(int, input().split())
a = list(map(int, input().split()))

# 2포인터 스택이용하기
st = deque()
st.append(a[0])
idx = 1
now_value = a[0]
ans = 0
while idx <= n:
    # print(now_value, st, idx)
    if now_value == m:
       ans += 1
    if now_value < m:
        if idx == n:
            break
        st.append(a[idx])
        now_value += a[idx]
        idx += 1
    else:
        now_value -= st.popleft()

print(ans)


# dp로 접근.. 시간초과
# data = [[0] * i for i in range(1, n+1)]
# # pprint(data)
# data[0][0] = a[0]
#
# cnt = 0
#
# for i in range(1, n):
#     for j in range(i+1):
#         if j == i:
#             data[i][j] = a[i]
#         else:
#             data[i][j] = data[i-1][j] + a[i]
#         if data[i][j] == m:
#             cnt += 1
# # pprint(data)
# print(cnt)
