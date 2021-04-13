import sys
a = list(map(int, sys.stdin.readline().rstrip().split()))
while 1:
    try:
        print(a[0]+a[1])
        a = list(map(int, sys.stdin.readline().rstrip().split()))
    except:
        break
