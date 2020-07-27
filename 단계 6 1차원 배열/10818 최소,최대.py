import sys

n = int(sys.stdin.readline().rstrip())
d = list(map(int, sys.stdin.readline().rstrip().split()))

# 소트로 푸는 법
d.sort()
print(d[0], d[len(d)-1])

# for문으로 정렬해서 푸는 법
# 100만이면 1초 넘지않나? n2하면

# min max 사용
# print(min(d),max(d))