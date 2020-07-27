import sys

d = list()
for i in range(9):

    #여기가 문제였음.. int 안넣으니 문자열로 인식한거같음
    d.append(int(sys.stdin.readline().rstrip()))

# ans = d.copy()
# ans.sort(reverse=True)
# # print(ans, d)
# ans2 = 0
# ans3 = 0
# for i in range(len(d)):
#     if d[i] == ans[0]:
#         ans2 = d[i]
#         ans3 = i+1
#         break
# print(ans2)
# print(ans3)
print(max(d))
print(d.index(max(d))+1)