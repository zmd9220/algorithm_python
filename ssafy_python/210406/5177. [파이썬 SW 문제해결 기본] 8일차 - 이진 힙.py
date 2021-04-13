
def is_small(n):
    parent = n // 2
    # 루트가 아닌 경우
    if parent:
        # 자식 노드 < 부모 노드 -> 체인지
        if tree[n] < tree[parent]:
            tree[n], tree[parent] = tree[parent], tree[n]
        # 루트 도착할 때 까지 재귀
        is_small(parent)
    # 루트인 경우 나감
    else:
        return


def sum_parents(n):
    parent = n // 2
    if parent:
        return tree[n]+sum_parents(parent)
    else:
        return tree[n]


for t in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    tree = [0] * (n+1)
    for i in range(len(data)):
        tree[i+1] = data[i]
        is_small(i+1)
    ans = sum_parents(n//2)
    print(f'#{t+1} {ans}')

