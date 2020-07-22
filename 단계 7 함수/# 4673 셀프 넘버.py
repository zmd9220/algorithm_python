def self_number(a, b :list):
    for i in range(1, a+1):
        sum = i
        tmp = i
        while True:
            if(tmp == 0):
                break
            sum += tmp % 10
            tmp = int(tmp / 10)
        if(sum <= 10001):
            b[sum] = 1


ans = [0 for i in range(10002)]
# print(ans)
self_number(10000, ans)

for i in range(1, 10001):
    if ans[i] == 0:
        print(i)

# 어려웠다.. c++보다 더 어렵네..