import sys

a = list(map(int, sys.stdin.readline().rstrip().split()))

# if 문 이용
for i in range(len(a)):
    for j in range(2):
        if a[j] <= a[j+1]:
            tmp = a[j]
            a[j] = a[j+1]
            a[j+1] = tmp
print(a[1])


# sort 이용
# a.sort()
# print(a[1])