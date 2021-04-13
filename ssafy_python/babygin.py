
num = 123444
ls = [0] * 12 # 12로 만드는 이유 - 나중에 run 계산할때 9번인덱스 검색한다면 9+1, 9+2 부분에서 인덱스 에러생김
nums = num
# 해당 숫자만큼 카운트해서 각 인덱스에 넣기(현재 123444에선 4번인덱스에 3개 123인덱스엔 각자1개씩)
while nums > 0:
    ls[nums % 10] += 1
    nums //= 10

i = 0
tri = run = 0
while i < 10:
    # 트리플 여부 검사
    if ls[i] >= 3:
        ls[i] -= 3
        tri += 1
        continue


# # 베이비진을 6중 for문을 이용하여 완전 검색으로 구현
# # --------------------------------
# def babyjin(data):
#     for i1 in range(6):
#         for i2 in range(6):
#             if i2 != i1 :
#                 for i3 in range(6):
#                     if i3 != i1 and i3 != i2 :
#                         for i4 in range(6):
#                             if i4 != i1 and i4 != i2 and i4 != i3:
#                                 for i5 in range(6):
#                                     if i5 != i1 and i5 != i2 and i5 != i3 and i5 != i4:
#                                         for i6 in range(6):
#                                             if i6 != i1 and i6 != i2 and i6 != i3 and i6 != i4 and i6 != i5:
#                                                 chk=0
#                                                 if data[i1]==data[i2] and data[i2]==data[i3]:
#                                                     chk+=1
#                                                 if data[i4] == data[i5] and data[i5] == data[i6]:
#                                                     chk += 1
#                                                 if data[i1]+1 == data[i2] and data[i2]+1 == data[i3]:
#                                                     chk += 1
#                                                 if data[i4]+1 == data[i5] and data[i5]+1 == data[i6]:
#                                                     chk += 1
#                                                 if chk==2:
#                                                     return True
#     return False
#
# data=[1, 2, 1, 9, 1, 4]
# if babyjin(data):
#     print("BabyJin")
# else:
#     print("Not")