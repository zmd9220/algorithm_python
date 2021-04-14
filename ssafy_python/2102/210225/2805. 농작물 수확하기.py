# 가운데 마름모 별찍기를 이용해서 인덱스접근

for t in range(int(input())):
    n = int(input())
    arr = []
    for i in range(n):
        tmp = input()
        tmp_ls = list(map(int, tmp))
        # print(tmp_ls)
        arr.append(tmp_ls)
    # arr = [list(map(int, input().split())) for _ in range(n)]
    mid = n//2
    result = 0
    # 파이썬에서 for 범위는 해당 범위 '전' 까지므로 범위 지정에 주의
    for i in range(mid+1):
        for j in range(mid-i, mid+i+1):
            result += arr[i][j]
    # for 의 시작점은 해당 '지점' 부터임
    for i in range(mid-1, -1, -1):
        for j in range(mid-i, mid+i+1):
            result += arr[n-i-1][j]

    print('#{} {}'.format(t+1, result))

# 참고 별찍기
# for t in range(int(input())):
#     n = int(input())
#     # arr = [list(map(int, input().split())) for _ in range(n)]
#     mid = n//2 + 1
#     for i in range(1, n+1):
#         for j in range(abs(mid-i)):
#             # print(' ', end='')
#         for j in range((mid-abs(mid-i))*2 - 1):
#             # print('*', end='')
#         # print()

