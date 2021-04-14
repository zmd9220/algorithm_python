# palindrome = arr[0][:m]
# print(palindrome)

# 보이어 무어 같은 문자열 찾는 알고리즘(패턴 매칭)이 회문에도 쓸 줄 알았는데 안쓰이네..
# 일반적인 팰린드롬으로 풀어보기
# 이 문제의 경우 회문이 딱 1개 존재하므로 찾으면 바로 break 걸면됨

# for t in range(int(input())):
#     n, m = map(int, input().split())
#     arr = [input() for _ in range(n)]
#     # 전체 회문은 m 크기여야 하므로 n-m 인덱스 이상의 인덱스들의 문자열은 m보다 작은 문자열이 됨
#     # 단 현재 range의 경우 해당 숫자 전까지 이므로 +1 해주기
#     # 또 가로 비교 세로 비교 두가지 경우로 나눠서 진행
#     result = ''
#     # 1. 가로 비교
#     for i in range(n):
#         for j in range(n-m+1):
#             palindrome = arr[i][j:j+m]
#             flag = True
#             for k in range(m//2):
#                 if palindrome[k] != palindrome[-1-k]:
#                     flag = False
#                     break
#             if flag:
#                 result = palindrome
#                 break
#     # 만약 위에서 회문 찾았으면 세로 비교는 무의미 그래서 못 찾았을 경우만 탐색
#     if not result:
#         # 2. 세로 비교
#         for i in range(n-m+1):
#             for j in range(n):
#                 flag = True
#                 tmp = ''
#                 for k in range(m):
#                     tmp += arr[i + k][j]
#                 for k in range(m//2):
#                     if tmp[k] != tmp[-1-k]:
#                         flag = False
#                         break
#                 if flag:
#                     result = tmp
#                     break
#
#
#     print('#{} {}'.format(t+1, result))

# for k in range(m//2):
#     if arr[k][j] != arr[-(m-i)-k][j]:
#         flag = False
#         break
# if flag:
#     for k in range(m):
#         result += arr[i + k][j]
#     break

