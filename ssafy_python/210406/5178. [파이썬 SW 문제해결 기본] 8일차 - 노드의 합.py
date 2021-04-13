# 루트 까지 올라가면서 시작했던 리프 노드 값을 다 더해줌
# tree_idx 현재 위치, start_idx 시작했던 위치(해당 위치 값을 더해줄 것이므로 필요)
def make_parent_value(tree_idx, start_idx):
    parent = tree_idx // 2
    if parent:
        tree[parent] += tree[start_idx]
        make_parent_value(parent, start_idx)
    return


for t in range(int(input())):
    n, m, l = map(int, input().split())
    tree = [0] * (n+1)
    for i in range(m):
        tree_idx, value = map(int, input().split())
        tree[tree_idx] = value
        make_parent_value(tree_idx, tree_idx)
    print(f'#{t+1} {tree[l]}')