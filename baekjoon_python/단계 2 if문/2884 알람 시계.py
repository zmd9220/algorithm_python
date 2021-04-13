import sys
# 쉽게 2개 변수 받는법
a, b = map(int, sys.stdin.readline().rstrip().split())
if b>=45:
    print(a,b-45)
else:
    # 45보다 작으면 시간을 바꿈
    if a == 0:
        print(23,b+15)
    else:
        print(a-1,b+15)