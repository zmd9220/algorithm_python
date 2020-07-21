import sys

n = int(sys.stdin.readline().rstrip())

for i in range(1, 2*n+1):
    if i%2 == 1:
        for j in range(1, n+1):
            if j%2 == 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    else:
        for j in range(1, n+1):
            if j % 2 == 1:
                print(" ", end="")
            else:
                print("*", end="")
        print()
