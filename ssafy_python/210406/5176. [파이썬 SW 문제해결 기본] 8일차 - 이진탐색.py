
def inorder(tr, now, n):
    global cnt
    if now <= n:
        inorder(tr, now*2, n)
        tr[now] = cnt
        cnt += 1
        inorder(tr, now*2 + 1, n)


for t in range(int(input())):
    n = int(input())
    cnt = 1
    tree = [0] * (n+1)
    inorder(tree, 1, n)
    print('#{} {} {}'.format(t+1, tree[1], tree[n//2]))