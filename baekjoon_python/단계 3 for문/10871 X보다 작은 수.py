import sys
a, b = map(int, sys.stdin.readline().rstrip().split())
c = list(map(int, sys.stdin.readline().rstrip().split()))
d = list()
for i in range(a):
    if c[i] < b:
        d.append(c[i])

for i in range(len(d)):
    print(d[i], end=' ') # end가 끝을 바꿔주는 것 기본은 \n
