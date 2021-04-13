
# 카운트 세는 순회 만들기가 생각보다 어려웠음;;

def preorder(n):
    cnt = 1
    left = 0
    right = 0
    if tree[n * 2] != 0:
        left = preorder(tree[n * 2])
    if tree[n * 2 + 1] != 0:
        right = preorder(tree[n * 2 + 1])
    cnt += left+right
    return cnt


for t in range(int(input())):
    e, n = map(int, input().split())
    edges = list(map(int, input().split()))
    # 위치를 담은 트리 생성, + 2 하는 이유는 0번 인덱스를 쓰지 않으므로 2*(e+1) + 1번 인덱스까지 활용하기 때문
    tree = [0] * (2 * (e+1) + 2)
    for i in range(0, len(edges), 2):
        if tree[edges[i] * 2]:
            tree[edges[i] * 2 + 1] = edges[i + 1]
        else:
            tree[edges[i] * 2] = edges[i + 1]
    ans = preorder(n)
    print('#{} {}'.format(t+1, ans))
