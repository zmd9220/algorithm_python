# reverse 함수나 slice notation을 빼고 다른 방법으로 문자열 뒤집기

st = 'algorithm'

# for i in range(len(st)-1, -1, -1):
#     print(st[i], end='')
# print()
print(st)
ls = list(st)
for i in range(len(st)//2):
    ls[i], ls[-1-i] = ls[-1-i], ls[i]

    st = ''.join(ls)

print(st)