import sys

l = list()
for i in range(5):
    a = int(sys.stdin.readline().rstrip())
    if a < 40:
        l.append(40)
    else:
        l.append(a)
ans = 0
for i in range(len(l)):
    ans += l[i]
print(int(ans/len(l)))