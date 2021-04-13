
def inorder(nodes, data, node):
    if nodes[node * 2] != 0:
        inorder(nodes, data, nodes[node * 2])
    print(data[node], end='')
    if nodes[node * 2 + 1] != 0:
        inorder(nodes, data, nodes[node * 2 + 1])


for t in range(1, 11):
    n = int(input())
    # arr = list(map(int, input().split()))
    # child = [[0] * 2 for i in range(n + 1)]
    nodes = [0] * (n * 2 + 2)
    data = [''] * (n+1)
    for i in range(1, n+1):
        tmp = list(input().split())
        idx = int(tmp[0])
        for j in range(1, len(tmp)):
            if tmp[j].isdigit():
                if nodes[idx * 2] != 0:
                    nodes[idx * 2 + 1] = int(tmp[j])
                else:
                    nodes[idx * 2] = int(tmp[j])
            else:
                data[idx] = tmp[j]
    print('#{} '.format(t))
    inorder(nodes, data, 1)
    print()
