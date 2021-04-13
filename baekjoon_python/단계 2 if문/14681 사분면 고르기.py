import sys
a = int(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline().rstrip())
if a>0:
    if b>0:
        print(1)
    else:
        print(4)
else:
    if b>0:
        print(2)
    else:
        print(3)