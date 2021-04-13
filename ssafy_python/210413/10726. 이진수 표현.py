
for t in range(int(input())):
    n, m = map(int, input().split())
    binary = ''
    ans = 'ON'
    while m > 1:
        if m % 2:
            binary += '1'
        else:
            binary += '0'
        m //= 2
    binary += str(m)
    # ans = ans[::-1]
    # print(ans)
    # print(binary)
    if len(binary) >= n:
        for i in range(n-1, -1, -1):
            if binary[i] != '1':
                ans = 'OFF'
                break
    # 애초에 확인할 비트가 전체 이진수 크기보다 큰 경우 그 위는 다 0이므로 off
    else:
        ans = 'OFF'
    print('#{} {}'.format(t+1, ans))

# for tc in range(1, int(input()) + 1):
#     n, m = map(int, input().split())
#
#     res = ''
#
#     if m == 0:
#         res = '0'
#
#     while m:
#         m, binary = divmod(m, 2)
#         res = str(binary) + res
#
#     val = res[-n:]
#     if val == '1' * n:
#         print(f'#{tc} ON')
#     else:
#         print(f'#{tc} OFF')

# for t in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     ans = 'ON' if ((1 << N)-1) & M == ((1 << N)-1) else 'OFF'
#     print('#{} {}'.format(t, ans))

# T = int(input())
# for tc in range(1, T+1):
#     print('#{}'.format(tc), end=' ')
#     N, M = map(int, input().split())
#     for i in range(N):
#         if bin(M)[-i-1] != '1':
#             print('OFF')
#             break
#     else:
#         print('ON')

# T=int(input())
# for tc in range(1,T+1):
#     #N,M일때 M의 이진수 표현의 마지막 N비트가 모두 1인지 확인
#     N,M = map(int,input().split())
#     tmp = '1'*N
#     chk = bin(M)[2:]
#     n_chk = len(chk)
#     if n_chk >= N:
#         if chk[n_chk-N:] == tmp:
#             res = 'ON'
#         else:
#             res = 'OFF'
#     else:
#         res='OFF'
#     print('#{} {}'.format(tc,res))