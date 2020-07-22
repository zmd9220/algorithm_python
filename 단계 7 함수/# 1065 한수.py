import sys


# 생각보다 꼬였음.. 은근 어려운 문제
def hans(ans, n):
    if n < 99:
        ans = n
    else:
        lst = list()
        for i in range(1, n+1):
            if i == 1000:
                break
            if i < 100:
                ans += 1
                continue
            else:
                tmp = i
                while tmp > 0:
                    lst.append(tmp % 10)
                    tmp = int(tmp / 10)
                if (lst[1]-lst[0] == lst[2]-lst[1]):
                    ans += 1
                lst.clear()
    return ans

n = int(sys.stdin.readline().rstrip())
ans = 0
print(hans(ans, n))
