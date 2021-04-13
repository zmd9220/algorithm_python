import sys

n = int(sys.stdin.readline().rstrip())

for i in range(2*n-1):
    if i < n:
        print(' ' * (i) + '*' * (2*(n-i)-1) + ' ' * (n-i))
    else:
        print(' ' * (2*(n-1)-i) + '*' * (2*(i-n+1)+1))

# 아직 안품