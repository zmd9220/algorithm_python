
def find_set(num):
    while arr[num] != num:
        num = arr[num]
    return num


def union(base_el, change_el):
    arr[find_set(change_el)] = find_set(base_el)


for t in range(int(input())):
    n, m = map(int, input().split())
    # make_set
    arr = [i for i in range(n+1)]
    group = list(map(int, input().split()))
    # 조 짜기 작업
    for i in range(m):
        base, change = group[i*2], group[i*2+1]
        union(base, change)
    ans = set()
    # 조 찾기 (대표 원소 갯수 찾기)
    for i in range(1, n+1):
        ans.add(find_set(i))
    print('#{} {}'.format(t+1, len(ans)))
