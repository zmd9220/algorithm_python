import sys

n = int(sys.stdin.readline().rstrip())
count = 0
ans = n
while True:
    count += 1
    a = int(ans / 10)
    b = int(ans % 10)
    c = int((a + b) % 10)
    # print(a,b,c)
    ans = b * 10 + c
    # print(ans)
    if n == ans:
        break

print(count)