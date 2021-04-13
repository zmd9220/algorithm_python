
# 보이어 무어 같은 문자열 찾는 알고리즘(패턴 매칭)이 회문에도 쓸 줄 알았는데 안쓰이네..
# 일반적인 팰린드롬으로 풀어보기
# 이 문제의 경우 회문이 딱 1개 존재하므로 찾으면 바로 break 걸면됨


# TC = int(input())
#
# for tc in range(1, TC+1):
#     N, M = map(int, input().split())
#     result = []
#
#     #가로줄 확인
#     Garo_lst = []
#     for i in range(N):
#         Data = input()
#         Garo_lst.append(Data)
#         for i in range(len(Data)-M+1):
#             if Data[i:M+i] == Data[i:M+i][::-1]:
#                 result.append(Data[i:M+i])
#
#     #세로줄 확인
#     Sero_lst = []
#     Sero_sub_lst = ''
#     for x in range(N):
#         for y in Garo_lst:
#             Sero_sub_lst += y[x]
#         Sero_lst.append(Sero_sub_lst)
#         Sero_sub_lst =''
#     print(Sero_lst)
#
#     for sero_data in Sero_lst:
#         for j in range(len(sero_data)-M+1):
#             print(sero_data[j:M + j])
#             if sero_data[j:M+j] == sero_data[j:M+j][::-1]:
#                 result.append(sero_data[j:M+j])
#
#     # print(result)
#     print("#%d %s"%(tc, result[0]))
