
a, b, c = map(int, input().split())
# a+bx < cx
# a < (c-b)x
# a / (c-b) < x

if b >= c:
    print(-1)
else:
    # ans = 1
    # income = c
    # while True:
    #     a += b
    #     if income > a:
    #         print(ans)
    #         break
    #     income += c
    #     ans += 1
    print(a//(c-b) + 1)