import sys

n = int(sys.stdin.readline().rstrip())
for i in range(1, n+1):
    print(' ' * (n-i) + '*' * i)

# c++의 경우 이중 포문 ' '처리용 for문, *처리용 for문