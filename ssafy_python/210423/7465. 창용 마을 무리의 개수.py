# 상호 배타 집합 개념을 이용
def find_set(num):
    while p[num] != num:
        num = p[num]
    return num


def union(base_el, change_el):
    p[find_set(change_el)] = find_set(base_el)


for t in range(int(input())):
    n, m = map(int, input().split())
    p = [i for i in range(n+1)] # make_set
    for i in range(m):
        base, change = map(int, input().split())
        union(base, change)
    ans = 0
    for i in range(1, n+1):
        if p[i] == i:
            ans += 1
    print('#{} {}'.format(t+1, ans))