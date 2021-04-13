# arr = [-2, 1, 9, 3, 4, -3, 5, -6, 8, 2]
#
# for i in range(1 << len(arr)):
#     for j in range(len(arr)+1):
#         if i & (i << j):
#             print(arr[j], end=', ')
#     print()
# print()

# input data: -2 1 9 3 4 -3 5 -6 8 2

N=10
K=0
arr=[-2, 1, 9, 3, 4, -3, 5, -6, 8, 2]
cnt=0
for i in range(1<<N):
    SUM=0
    sub=[]
    for j in range(N):
        if i & (1<<j):
            sub.append(arr[j])
            SUM += arr[j]

    if SUM==K:
        cnt+=1
        print(sub)
print("{}".format(cnt))