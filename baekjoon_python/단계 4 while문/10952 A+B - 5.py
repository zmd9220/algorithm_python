import sys
a = list(map(int, sys.stdin.readline().rstrip().split()))
while a[0] != 0 and a[1] != 0:
    print(a[0]+a[1])
    a = list(map(int, sys.stdin.readline().rstrip().split()))
