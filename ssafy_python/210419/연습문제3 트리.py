
def preorder(now_vertex):
    if now_vertex != 0:
        print(now_vertex, end=' ')
        preorder(child_node[now_vertex][0])
        preorder(child_node[now_vertex][1])


def inorder(now_vertex):
    if now_vertex != 0:
        inorder(child_node[now_vertex][0])
        print(now_vertex, end=' ')
        inorder(child_node[now_vertex][1])


def postorder(now_vertex):
    if now_vertex != 0:
        postorder(child_node[now_vertex][0])
        postorder(child_node[now_vertex][1])
        print(now_vertex, end=' ')


vertex = 13
arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7,
       5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]
child_node = [[0] * 2 for _ in range(vertex+1)]
for i in range(0, len(arr), 2):
    if child_node[arr[i]][0] == 0:
        child_node[arr[i]][0] = arr[i+1]
    else:
        child_node[arr[i]][1] = arr[i+1]
print(child_node)
print('preorder : ', preorder(1))
print('inorder : ', inorder(1))
print('postorder : ', postorder(1))
