def preorder(n):
    if n != 0:
        print(n, end=" ")
        left = child[arr[n]][0]
        right = child[arr[n]][1]
        if left != 0:
            preorder(left)
        if right != 0:
            preorder(right)
        return None


N = int(input())
arr = list(map(int, input().split()))
child = [[0] * 2 for i in range(N + 1)]
for i in range(N - 1):
    if child[arr[i * 2]][0] == 0:
        child[arr[i * 2]][0] = arr[i * 2 + 1]
    else:
        child[arr[i * 2]][1] = arr[i * 2 + 1]

print("전위 순회 결과:", end=" ")
preorder(1)
print()
